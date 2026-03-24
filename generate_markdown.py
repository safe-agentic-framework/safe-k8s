#!/usr/bin/env python3
"""Generate markdown pages for the SAFE-K8S public security control catalog."""

from __future__ import annotations

import re
from os.path import relpath
from collections import defaultdict
from pathlib import Path

import yaml


BASE_DIR = Path(__file__).resolve().parent
MARKDOWN_DIR = BASE_DIR / "markdown"
CONTROLS_DIR = MARKDOWN_DIR / "controls"
FRAMEWORKS_DIR = MARKDOWN_DIR / "frameworks"


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "item"


def md_escape(value: str | None) -> str:
    if value is None:
        return ""
    return str(value).replace("\r\n", "\n").strip()


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def link_to(from_path: Path, to_path: Path) -> str:
    return relpath(to_path, start=from_path.parent).replace("\\", "/")


def load_yaml(name: str):
    return yaml.safe_load((BASE_DIR / name).read_text(encoding="utf-8"))


def knowledge_area_anchor(knowledge_area_id: str) -> str:
    return slugify(f"knowledge-area-{knowledge_area_id}")


def summarize_knowledge_area(area_controls: list[dict]) -> str:
    if not area_controls:
        return "This knowledge area is represented by the control set below."

    focus_titles = [control["control_title"] for control in area_controls[:5]]
    if len(focus_titles) == 1:
        summary = focus_titles[0]
    elif len(focus_titles) == 2:
        summary = f"{focus_titles[0]} and {focus_titles[1]}"
    else:
        summary = ", ".join(focus_titles[:-1]) + f", and {focus_titles[-1]}"

    sentence = f"This knowledge area focuses on: {summary}."
    if len(area_controls) > len(focus_titles):
        sentence += " Additional controls in the table below extend this coverage."
    return sentence


def render_top_readme(domains, knowledge_areas, controls, crosswalks, framework_pages):
    controls_by_knowledge_area: dict[str, list[dict]] = defaultdict(list)
    for control in controls:
        controls_by_knowledge_area[control["knowledge_area"]].append(control)

    lines = [
        "# SAFE-K8S Public Security Control Catalog",
        "",
        "This repository publishes the public SAFE-K8S security control catalog for Kubernetes and AI systems. It includes the public control set, knowledge area structure, and framework crosswalks under `SAFE-K8S-*` identifiers.",
        "",
        "## Purpose",
        "",
        "- Publish a public SAFE-K8S control catalog for external use",
        "- Preserve traceability between controls and mapped frameworks",
        "- Support review, reuse, and downstream publication without internal-only fields",
        "",
        "## Contents",
        "",
        "- YAML source files for domains, knowledge areas, controls, and crosswalks",
        "- Generated markdown pages for controls and reverse mappings by framework",
        "",
        "## Basic Info",
        "",
        f"- Domains: {len(domains)}",
        f"- Knowledge areas: {len(knowledge_areas)}",
        f"- Controls: {len(controls)}",
        f"- Crosswalk rows: {len(crosswalks)}",
        "",
        "## YAML Files",
        "",
        "- `safe_k8s_domains.yaml`",
        "- `safe_k8s_knowledge_areas.yaml`",
        "- `safe_k8s_controls.yaml`",
        "- `safe_k8s_crosswalks.yaml`",
        "",
        "## Markdown Pages",
        "",
        "- `markdown/controls/` contains one markdown page per control with related mappings",
        "- `markdown/frameworks/` contains reverse-mapping pages by framework and requirement",
        "",
        "## Framework Reverse Mappings",
        "",
    ]
    for title, relpath in framework_pages:
        lines.append(f"- [{title}]({relpath})")
    lines.append("")
    lines.append("## Notes")
    lines.append("")
    lines.append("- Crosswalk pages keep `framework_mapping_notes` because they carry useful interpretive context.")
    lines.append("- `strength_reason_note` is intentionally not published in this export.")
    lines.append("")
    lines.append("## Knowledge Areas")
    lines.append("")
    for knowledge_area in knowledge_areas:
        anchor = knowledge_area_anchor(knowledge_area["knowledge_area"])
        lines.append(
            f"- [{knowledge_area['knowledge_area']} - {knowledge_area['knowledge_area_name']}](#{anchor})"
        )

    for knowledge_area in knowledge_areas:
        area_controls = controls_by_knowledge_area.get(knowledge_area["knowledge_area"], [])
        anchor = knowledge_area_anchor(knowledge_area["knowledge_area"])
        lines.extend(
            [
                "",
                f'<a id="{anchor}"></a>',
                f"## {knowledge_area['knowledge_area']} - {knowledge_area['knowledge_area_name']}",
                "",
                f"- Domain: {knowledge_area['domain_code']} - {knowledge_area['domain_name']}",
                f"- Maturity: {knowledge_area['maturity']}",
                f"- Controls: {len(area_controls)}",
                "",
                "### Description",
                "",
                summarize_knowledge_area(area_controls),
                "",
                "### Controls",
                "",
                "| Control ID | Title | Maturity | Class |",
                "| --- | --- | --- | --- |",
            ]
        )
        for control in area_controls:
            control_link = f"markdown/controls/{control['control_id']}.md"
            lines.append(
                f"| [{control['control_id']}]({control_link}) | {control['control_title']} | {control['maturity']} | {control['baseline_or_ai_specific']} |"
            )
    return "\n".join(lines)


def main() -> int:
    domains = load_yaml("safe_k8s_domains.yaml")
    knowledge_areas = load_yaml("safe_k8s_knowledge_areas.yaml")
    controls = load_yaml("safe_k8s_controls.yaml")
    crosswalks = load_yaml("safe_k8s_crosswalks.yaml")

    knowledge_by_id = {item["knowledge_area"]: item for item in knowledge_areas}
    control_by_id = {item["control_id"]: item for item in controls}

    mappings_by_control: dict[str, list[dict]] = defaultdict(list)
    mappings_by_framework: dict[tuple[str, str, str], list[dict]] = defaultdict(list)
    mappings_by_requirement: dict[tuple[str, str, str, str], list[dict]] = defaultdict(list)

    for row in crosswalks:
        mappings_by_control[row["control_id"]].append(row)
        fw_key = (row["framework_code"], row["framework_name"], row["framework_version"])
        req_key = fw_key + (row["framework_requirement_id"],)
        mappings_by_framework[fw_key].append(row)
        mappings_by_requirement[req_key].append(row)

    for control in controls:
        ka = knowledge_by_id.get(control["knowledge_area"])
        title = f"{control['control_id']} - {control['control_title']}"
        lines = [
            f"# {title}",
            "",
            f"- Domain: {control['domain_code']} - {control['domain_name']}",
            f"- Knowledge Area: {control['knowledge_area']} - {ka['knowledge_area_name'] if ka else ''}",
            f"- Maturity: {control['maturity']}",
            f"- Classification: {control['baseline_or_ai_specific']}",
        ]
        if control.get("superseded_by_control_id"):
            lines.append(f"- Superseded By: {control['superseded_by_control_id']}")
        lines.extend(
            [
                "",
                "## Statement",
                "",
                md_escape(control.get("control_statement")),
                "",
                "## Objective",
                "",
                md_escape(control.get("objective")),
                "",
                "## Rationale",
                "",
                md_escape(control.get("rationale")),
                "",
                "## Scope",
                "",
                md_escape(control.get("scope")),
                "",
                "## Enforcement",
                "",
                f"- Primary Enforcement Point: {md_escape(control.get('primary_enforcement_point'))}",
                f"- Implementation Surface: {md_escape(control.get('implementation_surface'))}",
                f"- Owner Primary: {md_escape(control.get('owner_primary'))}",
                f"- Owner Supporting: {md_escape(control.get('owner_supporting'))}",
                "",
                "## Related Crosswalks",
                "",
            ]
        )
        control_page = CONTROLS_DIR / f"{control['control_id']}.md"
        related = mappings_by_control.get(control["control_id"], [])
        if related:
            for row in related:
                framework_slug = slugify(f"{row['framework_code']}-{row['framework_version']}")
                req_slug = slugify(row["framework_requirement_id"])
                req_page = FRAMEWORKS_DIR / framework_slug / f"{req_slug}.md"
                lines.extend(
                    [
                        f"### {row['framework_code']} {row['framework_requirement_id']}",
                        "",
                        f"- Framework: {row['framework_name']} {row['framework_version']}",
                        f"- Requirement Title: {row['framework_requirement_title']}",
                        f"- Relation Type: {row['relation_type']}",
                        f"- Strength: {row['strength_level']}",
                        f"- Applicability: {row['applicability']}",
                        f"- Strength Reason Code: {md_escape(row.get('strength_reason_code')) or 'n/a'}",
                    ]
                )
                if row.get("applicability_condition"):
                    lines.append(f"- Applicability Condition: {md_escape(row['applicability_condition'])}")
                lines.extend(
                    [
                        "",
                        "#### Framework Mapping Notes",
                        "",
                        md_escape(row.get("framework_mapping_notes")) or "None.",
                        "",
                        f"[Reverse Mapping Page]({link_to(control_page, req_page)})",
                        "",
                    ]
                )
        else:
            lines.append("No related crosswalk rows.")
        write(control_page, "\n".join(lines))

    framework_index_links: list[tuple[str, str]] = []
    for fw_key, rows in sorted(mappings_by_framework.items()):
        framework_code, framework_name, framework_version = fw_key
        framework_slug = slugify(f"{framework_code}-{framework_version}")
        framework_dir = FRAMEWORKS_DIR / framework_slug
        req_ids = sorted({row["framework_requirement_id"] for row in rows})
        title = f"{framework_name} {framework_version}"
        readme_lines = [
            f"# {title}",
            "",
            f"- Framework Code: {framework_code}",
            f"- Version: {framework_version}",
            f"- Total Reverse Mappings: {len(rows)}",
            f"- Distinct Requirements Mapped: {len(req_ids)}",
            "",
            "## Requirements",
            "",
        ]

        for req_id in req_ids:
            req_rows = mappings_by_requirement[(framework_code, framework_name, framework_version, req_id)]
            req_title = req_rows[0]["framework_requirement_title"]
            req_slug = slugify(req_id)
            req_page = framework_dir / f"{req_slug}.md"
            readme_lines.append(f"- [{req_id} - {req_title}]({req_slug}.md)")

            req_lines = [
                f"# {framework_name} {framework_version} - {req_id}",
                "",
                f"- Framework Code: {framework_code}",
                f"- Requirement Title: {req_title}",
                "",
                "## Mapping Notes",
                "",
                md_escape(req_rows[0].get("framework_mapping_notes")) or "None.",
                "",
                "## SAFE-K8S Controls",
                "",
            ]
            for row in req_rows:
                control = control_by_id[row["control_id"]]
                control_page = CONTROLS_DIR / f"{control['control_id']}.md"
                req_lines.extend(
                    [
                        f"### [{control['control_id']} - {control['control_title']}]({link_to(req_page, control_page)})",
                        "",
                        f"- Domain: {control['domain_code']} - {control['domain_name']}",
                        f"- Knowledge Area: {control['knowledge_area']}",
                        f"- Relation Type: {row['relation_type']}",
                        f"- Strength: {row['strength_level']}",
                        f"- Applicability: {row['applicability']}",
                        f"- Strength Reason Code: {md_escape(row.get('strength_reason_code')) or 'n/a'}",
                        "",
                    ]
                )
            write(req_page, "\n".join(req_lines))

        write(framework_dir / "README.md", "\n".join(readme_lines))
        framework_index_links.append(
            (
                title,
                (framework_dir / "README.md").relative_to(BASE_DIR).as_posix(),
            )
        )

    top_readme = render_top_readme(domains, knowledge_areas, controls, crosswalks, framework_index_links)
    write(BASE_DIR / "README.md", top_readme)
    print(f"Wrote markdown pages under {MARKDOWN_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
