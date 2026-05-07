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
  heading: "A member-owned dual-entity venture studio for independent film."
  # Body paragraphs are below in the markdown section: "# about-body"

# ----- OPERATING SYSTEM -----
# (YAML key remains "segments" so the URL fragment #segments still resolves;
# all user-facing copy now reflects the operating-system framing.)
segments:
  eyebrow: "Operating system"
  heading: "Two paired entities, one rulebook, three brands."
  lede: "INTERDEPENDENT applies the canonical dual-entity venture studio model — used widely in software venture creation — to independent film. Two paired entities, not parent and subsidiary: an operating company where the work happens, and an affiliated capital entity where institutional capital is raised. Inside each, several Series with isolated assets and liabilities under Delaware's Series statute. One Operating Agreement and one Economic Attribution Policy govern every Production. Three brands sit on top of the architecture and surface it to the world."
  items:
    - name:        "INTERDEPENDENT LLC"
      slug:        "Operating company"
      description: "The Delaware Series LLC where the work happens. Houses People (PeopleCo, employer of record), Studios and Productions (each film is its own Series), operating services (payroll, finance, the open-book ledger), physical infrastructure (FacilityCo, EquipmentCo, FleetCo), and IP (Media Library, Technology Library)."
      link_text:   ""
      link_url:    ""

    - name:        "INTERDEPENDENT Ventures LP"
      slug:        "Capital entity · affiliated"
      description: "The Delaware Series LP where institutional capital is raised. Anchor Fund I is current; Growth Fund II, International Fund III, and Permanent Capital Fund are planned. Operated alongside INTERDEPENDENT LLC; not a subsidiary."
      link_text:   "Inquire"
      link_url:    "mailto:hello@interdependent.llc?subject=Ventures%20inquiry"

    - name:        "INTERDEPENDENT"
      slug:        ".studio"
      description: "The online studio lot. The production and coordination platform Studio Series and their members use to run their slates."
      link_text:   "Visit"
      link_url:    "https://interdependent.studio"

    - name:        "INTERDEPENDENT"
      slug:        ".tv"
      description: "The audience and exhibition layer. Streaming, community, and events that connect completed productions to viewers."
      link_text:   "Visit"
      link_url:    "https://interdependent.tv"

    - name:        "Future-Proof Production Campus"
      slug:        "Global campus network"
      description: "Dual-use traditional production and AI/compute facilities, with permanent INTERDEPENDENT-branded theatrical venues at each location. Coudersport, Pennsylvania, is the first; the international network is in development with Hackman Capital Partners across the leading box-office markets."
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

INTERDEPENDENT applies the dual-entity venture studio model — the canonical structure that pairs an operating company, where staff sit and work happens, with a separate capital entity that raises institutional capital under conventional venture-fund norms — to independent film production. INTERDEPENDENT LLC is the operating company; INTERDEPENDENT Ventures LP is the affiliated capital entity. The two are paired, not parent and subsidiary.

Each production is a Series of INTERDEPENDENT LLC, with its own assets and liabilities legally isolated under Delaware's Series statute. Membership extends across every contributor role: writers, directors, crew, executive producers, and capital partners are all members with documented economic interests, granted through the role-based process defined in the Operating Agreement. The Operating Agreement governs the structure; the Economic Attribution Policy governs how every contribution becomes an interest. Together, they are the platform's published rulebook.

The rulebook is the studio. Where classical Hollywood enforced house style through contract talent and the studio lot, INTERDEPENDENT enforces it through the Operating Agreement, the Economic Attribution Policy, the Production Standards, and a published Cultural Performance Score — together, the constitution of the company's cultural identity. The pipeline runs as an open platform; the brand emerges from the standards every Production passes through.

# library-body

Every Production releases as "An INTERDEPENDENT Picture." Together, the films constitute INTERDEPENDENT Pictures — the unified studio library — held in permanent custody by the Media Library Series. The library compounds across Seasons; the Permanent Capital Vehicle treats it as an appreciating asset across decades.

The exhibition layer is built to compound with the library. INTERDEPENDENT runs its events through Plots Inc., an institutionally backed events platform whose investors include Andreessen Horowitz, Best Nights, and Ethos Fund. Inside Plots, a co-host network of vetted independent operators produces INTERDEPENDENT-branded events under shared standards and a revenue-share model. Across the global campus network in development with Hackman Capital Partners, each Future-Proof Production Campus operates a permanent INTERDEPENDENT-branded theatrical venue.

For the first time since the Paramount Consent Decrees were dismantled in 1948 — and re-permitted by their August 2022 termination — production, distribution, and exhibition under one company is legally available. INTERDEPENDENT is built inside that window.

# leadership-bio

Chris Amell founded INTERDEPENDENT in 2026 to organize independent film production around a published rulebook and a member-owned cap table. He is responsible for the strategic direction of the company and its operating system.
