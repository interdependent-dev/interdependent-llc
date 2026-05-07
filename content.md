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
  meta_description: "INTERDEPENDENT LLC is a member-owned dual-entity venture studio for independent film, operating across media, capital, and technology."
  og_title: "INTERDEPENDENT LLC"
  og_description: "A member-owned dual-entity venture studio for independent film, operating across media, capital, and technology."

# Top navigation bar — edit labels or add/remove links
nav:
  - { label: "About",            href: "#about" }
  - { label: "Operating System", href: "#segments" }
  - { label: "Library",          href: "#library" }
  - { label: "Governance",       href: "#governance" }
  - { label: "Leadership",       href: "#leadership" }
  - { label: "Contact",          href: "#contact" }

# ----- HERO -----
hero:
  eyebrow: "Delaware Series LLC · Established 2017"
  title_top: "INTERDEPENDENT"
  title_suffix: "LLC"
  statement: "A member-owned enterprise operating across media, capital, and technology."
  meta:
    - { label: "Form",         value: "Delaware Series LLC" }
    - { label: "Headquarters", value: "Coudersport, PA" }
    - { label: "Founded",      value: "2017" }

# ----- ABOUT -----
about:
  eyebrow: "The model"
  heading: "The studio system, reborn for independent film."
  # Body paragraphs are below in the markdown section: "# about-body"

# ----- OPERATING SYSTEM -----
# (YAML key remains "segments" so the URL fragment #segments still resolves;
# all user-facing copy now reflects the operating-system framing.)
segments:
  eyebrow: "Operating system"
  heading: "Two paired entities, three brands."
  lede: "An operating company paired with an affiliated capital entity — the dual-entity venture studio model, applied to film. Inside, every Production is its own Series with assets and liabilities legally isolated under Delaware's Series statute. Three brands surface the architecture to audiences and partners."
  items:
    - name:        "INTERDEPENDENT LLC"
      slug:        "Operating company"
      description: "The Delaware Series LLC. Houses production, employment, services, infrastructure, and IP."
      link_text:   ""
      link_url:    ""

    - name:        "INTERDEPENDENT Ventures LP"
      slug:        "Capital entity · affiliated"
      description: "The Delaware Series LP where institutional capital is raised. Anchor Fund I current; Funds II, III, and Permanent Capital planned. Operated alongside; not a subsidiary."
      link_text:   "Inquire"
      link_url:    "mailto:hello@interdependent.llc?subject=Ventures%20inquiry"

    - name:        "INTERDEPENDENT"
      slug:        ".studio"
      description: "The online studio lot. Production and coordination for Studios."
      link_text:   "Visit"
      link_url:    "https://interdependent.studio"

    - name:        "INTERDEPENDENT"
      slug:        ".tv"
      description: "The audience layer. Streaming, community, and events for completed productions."
      link_text:   "Visit"
      link_url:    "https://interdependent.tv"

    - name:        "Future-Proof Production Campus"
      slug:        "Global campus network"
      description: "Dual-use traditional and AI/compute facilities, with permanent INTERDEPENDENT theatrical venues. Coudersport first; international with Hackman Capital Partners."
      link_text:   "In development"
      link_url:    ""

# ----- LIBRARY AND EXHIBITION -----
library:
  eyebrow: "Library and exhibition"
  heading: "Every Production releases as an INTERDEPENDENT Picture."
  # Body paragraphs are below in the markdown section: "# library-body"

# ----- GOVERNANCE -----
governance:
  eyebrow: "Governance"
  heading: "A published rulebook, binding on every Production."
  lede: "Allocation, distribution, and decision rights are governed by the Operating Agreement and the Economic Attribution Policy. Both are signed and effective; both are available on request to qualified counterparties."
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

INTERDEPENDENT is a film studio designed for independent filmmakers. Every contributor — writer, director, crew, executive producer, capital partner — becomes a member of the company with a documented economic interest in the films they help make.

The structure is the venture studio model applied to film, inside the legal window opened by the August 2022 termination of the Paramount Consent Decrees.

# library-body

The films constitute INTERDEPENDENT Pictures — the unified studio library — held in permanent custody by the Media Library Series and treated as an appreciating cultural asset across decades.

Exhibition runs through Plots Inc. and a co-host network of vetted independent operators producing INTERDEPENDENT-branded events. Each Future-Proof Production Campus also operates a permanent INTERDEPENDENT theatrical venue.

# leadership-bio

He is responsible for INTERDEPENDENT's strategic direction, its governing documents, and the design of its operating system.
