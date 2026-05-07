---
# ============================================================
# CONTENT FILE — INTERDEPENDENT.LLC
# ============================================================
# Edit any value below. Save the file. Commit and push.
# The site rebuilds and deploys automatically (~60 seconds).
#
# Two formats live in this file:
#   1. YAML (this part, between the --- markers): structured fields,
#      labels, lists. Indentation matters — keep the spacing as-is.
#   2. Markdown (below the second ---): long-form prose paragraphs.
#
# If you only edit prose, you'll never touch YAML.
# ============================================================

site:
  meta_title: "INTERDEPENDENT LLC"
  meta_description: "INTERDEPENDENT LLC is a Delaware Series LLC operating across entertainment, capital, and technology."
  og_title: "INTERDEPENDENT LLC"
  og_description: "A Delaware Series LLC operating across entertainment, capital, and technology."

# Top navigation bar — edit labels or add/remove links
nav:
  - { label: "About",              href: "#about" }
  - { label: "Operating Segments", href: "#segments" }
  - { label: "Governance",         href: "#governance" }
  - { label: "Leadership",         href: "#leadership" }
  - { label: "Contact",            href: "#contact" }

# ----- HERO -----
hero:
  eyebrow: "Delaware Series LLC · Established 2026"
  title_top: "INTERDEPENDENT"
  title_suffix: "LLC"
  statement: "A holding company operating across entertainment, capital, and technology."
  meta:
    - { label: "Form",         value: "Delaware Series LLC" }
    - { label: "Headquarters", value: "Coudersport, PA" }
    - { label: "Founded",      value: "2026" }

# ----- ABOUT -----
about:
  eyebrow: "The company"
  heading: "A working company organized around a long view of independent media."
  # Body paragraphs are below in the markdown section: "# about-body"

# ----- OPERATING SEGMENTS -----
segments:
  eyebrow: "Operating segments"
  heading: "Four lines of business under one company."
  lede: "Each segment runs as its own brand and property. The governing entity sets policy, governance, and shared services."
  items:
    - name:        "INTERDEPENDENT Studio"
      slug:        ".studio"
      description: "The production platform. Development, pre-production, and hybrid traditional/generative production for film and series."
      link_text:   "Visit"
      link_url:    "https://interdependent.studio"

    - name:        "INTERDEPENDENT TV"
      slug:        ".tv"
      description: "The audience and exhibition layer. Streaming, community, and events that connect productions to viewers."
      link_text:   "Visit"
      link_url:    "https://interdependent.tv"

    - name:        "Future-Proof Production Campus"
      slug:        "Coudersport, PA"
      description: "A dual-use traditional production and AI/compute facility on existing fiber backbone in north-central Pennsylvania."
      link_text:   "In development"
      link_url:    ""

    - name:        "INTERDEPENDENT Ventures LP"
      slug:        "affiliated"
      description: "An affiliated Delaware Series Limited Partnership that finances productions through a separate fund structure. Operated alongside the company; not a subsidiary."
      link_text:   "Inquire"
      link_url:    "mailto:hello@interdependent.llc?subject=Ventures%20inquiry"

# ----- GOVERNANCE -----
governance:
  eyebrow: "Governance"
  heading: "Member-owned, with a single, published rulebook."
  lede: "Each contributor — capital partner, screenwriter, director, department head, crew, executive — is documented as a member with a defined economic interest. Allocation, distribution, and decision rights are governed by the Operating Agreement and the Economic Attribution Policy."
  rows:
    - { label: "Entity form",           value: "Delaware Series Limited Liability Company" }
    - { label: "Ownership",             value: "Privately held, member-owned" }
    - { label: "Governing instruments", value: "Operating Agreement and Economic Attribution Policy (signed and effective)" }
    - { label: "Series structure",      value: "Each production held in its own Series, with assets and liabilities legally separated" }
    - { label: "Affiliated capital",    value: "INTERDEPENDENT Ventures LP — separate Delaware Series Limited Partnership" }
    - { label: "Auditor & counsel",     value: "Engaged; available on request to qualified counterparties" }

# ----- LEADERSHIP -----
leadership:
  eyebrow: "Leadership"
  heading: "Founder & Executive Director."
  name:    "Christopher Gilbert Amell"
  title:   "Founder & Executive Director"
  # Bio paragraph is below in the markdown section: "# leadership-bio"

# ----- CONTACT -----
contact:
  eyebrow: "Contact"
  heading: "Direct inquiries reach the company quickly."
  blocks:
    - label:    "General & press"
      value:    "hello@interdependent.llc"
      kind:     "email"
    - label:    "Legal & compliance"
      value:    "legal@interdependent.llc"
      kind:     "email"
    - label:    "Mailing"
      kind:     "address"
      lines:
        - "INTERDEPENDENT LLC"
        - "712 North Main Street"
        - "Coudersport, PA 16915"
        - "United States"

# ----- FOOTER -----
footer:
  entity_line: "© 2026 INTERDEPENDENT LLC · A Delaware Series Limited Liability Company"
  links:
    - { label: "Privacy",  href: "privacy.html" }
    - { label: "Terms",    href: "terms.html" }
    - { label: "Contact",  href: "mailto:hello@interdependent.llc" }
---

# about-body

INTERDEPENDENT LLC is the parent operating entity for a group of related businesses in independent film production, audience and distribution platforms, and physical infrastructure. The company is organized as a Delaware Series LLC, with each production held in its own Series and governed by a single Operating Agreement and a published Economic Attribution Policy.

The company is privately held and member-owned. It operates the platforms and the campus directly, and works alongside an affiliated capital entity that finances productions through a separate fund structure.

# leadership-bio

Chris Amell founded INTERDEPENDENT in 2026 to organize independent film production around a published rulebook and a member-owned cap table. He is responsible for the strategic direction of the company and its operating segments.
