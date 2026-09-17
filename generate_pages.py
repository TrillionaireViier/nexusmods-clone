import os

pages = [
    ("privacy-policy", "Privacy Policy", "Learn about how we handle your data.", "Your privacy is important to us. This page outlines our data collection and usage policies..."),
    ("terms-of-service", "Terms of Service", "The rules and guidelines for using Nexus Mods.", "By using our platform, you agree to abide by these terms..."),
    ("cookie-policy", "Cookie Policy", "How we use cookies to improve your experience.", "We use cookies to keep you logged in and provide analytics..."),
    ("forums", "Forums", "Join the discussion in our community forums.", "Our forums are the best place to ask questions and share knowledge..."),
    ("discord", "Discord Server", "Join our official Discord community.", "Click here to join our Discord server and chat with thousands of other modders in real time!"),
    ("wiki", "Wiki", "Community-driven documentation and guides.", "Welcome to the Nexus Mods Wiki, maintained by our wonderful community..."),
    ("bug-reports", "Bug Reports", "Report issues with the site or specific mods.", "Found a bug? Let us know so we can fix it..."),
    ("feature-requests", "Feature Requests", "Suggest new features for the Nexus Mods platform.", "Have an idea to make Nexus Mods better? Share it here..."),
    ("help-center", "Help Center", "Find answers to frequently asked questions.", "Search our knowledge base for solutions to common problems..."),
    ("mod-manager", "Mod Manager", "Download and learn about our official mod manager.", "Vortex is our official, easy-to-use mod manager. Download it today!"),
    ("api-docs", "API Docs", "Documentation for developers building with the Nexus Mods API.", "Build incredible tools and integrations using our public API..."),
    ("contact-us", "Contact Us", "Get in touch with the Nexus Mods team.", "Need help with your account? Contact our support team..."),
    ("donate", "Donate", "Support the platform and our mod authors.", "Your donations keep the servers running and support the creators who make modding possible.")
]

template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} - Nexus Mods</title>
  <link rel="stylesheet" href="index.css" />
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%23d98f40'/%3E%3Ctext x='16' y='23' text-anchor='middle' font-family='Arial' font-weight='900' font-size='20' fill='%230d0f14'%3EN%3C/text%3E%3C/svg%3E" />
</head>
<body>
  <header class="main-header">
    <div class="header-inner">
      <a href="index.html" class="logo"><div class="logo-icon">N</div><div class="logo-text">NEXUS<span>MODS</span></div></a>
      <nav class="main-nav">
        <a href="index.html" class="nav-link">Home</a>
        <a href="games.html" class="nav-link">Games</a>
        <a href="mods.html" class="nav-link">Mods</a>
        <a href="community.html" class="nav-link">Community</a>
        <a href="collections.html" class="nav-link">Collections</a>
        <a href="news.html" class="nav-link">News</a>
      </nav>
      <div class="header-actions">
        <a href="login.html" class="btn btn-ghost" style="border: none;">Log In</a>
        <a href="signup.html" class="btn btn-primary">Register</a>
      </div>
    </div>
  </header>

  <section style="background: var(--bg-secondary); padding: var(--space-3xl) 0; border-bottom: 1px solid var(--border-subtle);">
    <div class="container">
      <h1 style="font-family:'Rajdhani';font-size:42px;">{title}</h1>
      <p style="color:var(--text-secondary);max-width:600px;">{subtitle}</p>
    </div>
  </section>

  <main class="container" style="padding-top: var(--space-2xl); padding-bottom: var(--space-3xl); min-height: 40vh;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: var(--radius-lg); padding: var(--space-2xl);">
      <p style="font-size: 16px; color: var(--text-primary); line-height: 1.8;">
        {content}
      </p>
      <div style="margin-top: var(--space-2xl); padding-top: var(--space-xl); border-top: 1px solid var(--border-subtle);">
        <p style="color: var(--text-tertiary); font-size: 14px;">Last updated: September 2026</p>
      </div>
    </div>
  </main>

  <footer class="main-footer">
    <div class="container">
      <div class="footer-bottom" style="border:none;padding:0;">
        <p class="footer-copyright">© 2024 Nexus Mods. All rights reserved.</p>
        <div class="footer-legal">
          <a href="privacy-policy.html">Privacy Policy</a>
          <a href="terms-of-service.html">Terms of Service</a>
          <a href="cookie-policy.html">Cookie Policy</a>
        </div>
      </div>
    </div>
  </footer>
</body>
</html>"""

for file_name, title, subtitle, content in pages:
    with open(f"{file_name}.html", "w") as f:
        f.write(template.format(title=title, subtitle=subtitle, content=content))
    print(f"Generated {file_name}.html")
