import os

pages = [
    ("forums", "Forums", "Join the discussion in our community forums.", """
        <h3 style="font-family:'Rajdhani'; font-size:24px; margin-bottom:12px;">Welcome to the Community</h3>
        <p style="margin-bottom:16px; color:var(--text-secondary);">The ViierMods forums are the central hub for modders and players alike. Whether you're looking for load order advice, troubleshooting a crash, or discussing the lore of your favorite RPG, you'll find a place here.</p>
        <ul style="margin-bottom:16px; color:var(--text-secondary); margin-left: 20px;">
            <li><strong>Modding Help:</strong> Get technical assistance from veteran mod authors.</li>
            <li><strong>Game Discussions:</strong> Talk about your favorite titles, upcoming releases, and general gaming news.</li>
            <li><strong>Author Feedback:</strong> Leave detailed feedback and bug reports directly for mod creators.</li>
        </ul>
        <a href="/community" class="btn btn-primary" style="display:inline-block; margin-top: 10px;">Go to Forums</a>
    """),
    ("discord", "Discord Server", "Join our official Discord community.", """
        <h3 style="font-family:'Rajdhani'; font-size:24px; margin-bottom:12px;">Real-Time Chat & Support</h3>
        <p style="margin-bottom:16px; color:var(--text-secondary);">Looking for instant answers or just want to hang out with fellow modders? Our official Discord server has over 50,000 active members and features dedicated channels for all major games.</p>
        <p style="margin-bottom:16px; color:var(--text-secondary);">Benefits of joining:</p>
        <ul style="margin-bottom:16px; color:var(--text-secondary); margin-left: 20px;">
            <li>Direct access to community managers and staff.</li>
            <li>Live voice channels for collaborative modding and gaming.</li>
            <li>Exclusive early-access announcements and beta testing opportunities.</li>
        </ul>
        <button class="btn btn-primary" style="display:inline-block; margin-top: 10px; background-color: #5865F2;">Join the Discord Server</button>
    """),
    ("wiki", "Wiki", "Community-driven documentation and guides.", """
        <h3 style="font-family:'Rajdhani'; font-size:24px; margin-bottom:12px;">The Modder's Knowledge Base</h3>
        <p style="margin-bottom:16px; color:var(--text-secondary);">The ViierMods Wiki is a collaborative repository of tutorials, modding tool documentation, and game-specific guides. Maintained entirely by our community, it is the ultimate resource for anyone looking to learn how to create mods from scratch.</p>
        <h3 style="font-family:'Rajdhani'; font-size:20px; margin-bottom:12px; margin-top: 24px;">Popular Guides:</h3>
        <ul style="margin-bottom:16px; color:var(--text-secondary); margin-left: 20px;">
            <li>Getting Started with the Creation Kit</li>
            <li>How to resolve mod conflicts with xEdit</li>
            <li>Creating your first custom 3D mesh</li>
            <li>Understanding Load Orders and sorting</li>
        </ul>
    """),
    ("bug-reports", "Bug Reports", "Report issues with the site or specific mods.", """
        <h3 style="font-family:'Rajdhani'; font-size:24px; margin-bottom:12px;">Help Us Improve</h3>
        <p style="margin-bottom:16px; color:var(--text-secondary);">Encountered a glitch on the website? Is a download button broken? Let our engineering team know by submitting a detailed bug report.</p>
        <div style="background: var(--bg-tertiary); padding: var(--space-md); border-radius: var(--radius-md); border: 1px solid var(--border-subtle); margin-bottom: 24px;">
            <p style="font-size: 14px; margin-bottom: 8px;"><strong>Note:</strong> This page is for reporting issues with the <em>ViierMods website</em> or <em>Mod Manager</em> itself. If a specific mod is crashing your game, please go to that mod's page and use the "Bugs" tab to notify the mod author directly.</p>
        </div>
        <form style="display: flex; flex-direction: column; gap: 16px; max-width: 500px;">
            <input type="text" placeholder="Issue Title (e.g., 'Search bar not working')" class="form-input" style="padding: 10px; border-radius: 4px; border: 1px solid var(--border-subtle); background: var(--bg-tertiary); color: white;">
            <textarea placeholder="Describe the steps to reproduce the bug..." rows="5" style="padding: 10px; border-radius: 4px; border: 1px solid var(--border-subtle); background: var(--bg-tertiary); color: white; resize: vertical;"></textarea>
            <button type="button" class="btn btn-primary" style="width: 150px;">Submit Report</button>
        </form>
    """),
    ("feature-requests", "Feature Requests", "Suggest new features for the platform.", """
        <h3 style="font-family:'Rajdhani'; font-size:24px; margin-bottom:12px;">Shape the Future of ViierMods</h3>
        <p style="margin-bottom:16px; color:var(--text-secondary);">Have a brilliant idea that would make finding, downloading, or managing mods easier? We actively review community suggestions to plan our development roadmap.</p>
        <h3 style="font-family:'Rajdhani'; font-size:20px; margin-bottom:12px; margin-top: 24px;">Recent Community Ideas Implemented:</h3>
        <ul style="margin-bottom:24px; color:var(--text-secondary); margin-left: 20px;">
            <li>Dark mode by default (Suggested by <em>ModKing99</em>)</li>
            <li>One-click collection downloads (Suggested by <em>SkyrimLover</em>)</li>
            <li>Integrated mod load order sorting (Suggested by <em>TheGuru</em>)</li>
        </ul>
        <button class="btn btn-ghost" style="display:inline-block;">Submit a New Idea</button>
    """),
    ("support", "Support", "Get help with your account and the platform.", """
        <h3 style="font-family:'Rajdhani'; font-size:24px; margin-bottom:12px;">How can we help?</h3>
        <p style="margin-bottom:16px; color:var(--text-secondary);">Our support team is available 24/7 to assist you with account recovery, billing inquiries, premium subscription management, and platform navigation.</p>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 24px;">
            <div style="background: var(--bg-tertiary); padding: 20px; border-radius: 8px; text-align: center;">
                <div style="font-size: 32px; margin-bottom: 10px;">🔐</div>
                <h4 style="margin-bottom: 10px;">Account Issues</h4>
                <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 15px;">Forgot your password or lost access to your 2FA app?</p>
                <a href="/contact-us" class="btn btn-ghost" style="font-size: 12px; padding: 5px 10px;">Reset Account</a>
            </div>
            <div style="background: var(--bg-tertiary); padding: 20px; border-radius: 8px; text-align: center;">
                <div style="font-size: 32px; margin-bottom: 10px;">💳</div>
                <h4 style="margin-bottom: 10px;">Billing & Premium</h4>
                <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 15px;">Questions about a recent charge or want to upgrade?</p>
                <a href="/premium" class="btn btn-ghost" style="font-size: 12px; padding: 5px 10px;">Manage Billing</a>
            </div>
        </div>
    """),
    ("help-center", "Help Center", "Find answers to frequently asked questions.", """
        <h3 style="font-family:'Rajdhani'; font-size:24px; margin-bottom:12px;">Frequently Asked Questions</h3>
        <p style="margin-bottom:24px; color:var(--text-secondary);">Browse our knowledge base to find quick answers to the most common questions from our users.</p>
        
        <div style="margin-bottom: 20px; border-bottom: 1px solid var(--border-subtle); padding-bottom: 15px;">
            <h4 style="margin-bottom: 8px; font-size: 18px;">How do I install mods?</h4>
            <p style="color: var(--text-secondary); font-size: 14px;">The easiest way is to download our official Mod Manager. Click the "Mod Manager Download" button on any mod page, and the application will handle the extraction and placement of files automatically.</p>
        </div>
        <div style="margin-bottom: 20px; border-bottom: 1px solid var(--border-subtle); padding-bottom: 15px;">
            <h4 style="margin-bottom: 8px; font-size: 18px;">Why is my download speed capped?</h4>
            <p style="color: var(--text-secondary); font-size: 14px;">Free users are capped at 2MB/s to ensure server stability for everyone. To unlock uncapped, ultra-fast downloads via our global CDN, consider upgrading to Premium.</p>
        </div>
        <div style="margin-bottom: 20px;">
            <h4 style="margin-bottom: 8px; font-size: 18px;">I forgot my password, what do I do?</h4>
            <p style="color: var(--text-secondary); font-size: 14px;">Go to the login page and click "Forgot Password". Enter your registered email address, and we will send you a secure link to reset your credentials.</p>
        </div>
    """),
    ("mod-manager", "Mod Manager", "Download and learn about our official mod manager.", """
        <h3 style="font-family:'Rajdhani'; font-size:24px; margin-bottom:12px;">Meet Vortex: The Ultimate Mod Manager</h3>
        <p style="margin-bottom:16px; color:var(--text-secondary);">Vortex is the new, modern mod manager from ViierMods. It is designed to make modding your game as simple as possible for new users, while still providing enough control for veterans.</p>
        
        <div style="display: flex; gap: 20px; align-items: center; margin-bottom: 30px; background: var(--bg-tertiary); padding: 20px; border-radius: 8px;">
            <div style="font-size: 48px;">⚙️</div>
            <div>
                <h4 style="margin-bottom: 5px;">One-Click Install</h4>
                <p style="font-size: 14px; color: var(--text-secondary);">Download mods directly from the website into Vortex, and install them into your game with a single click. No manual file extraction required.</p>
            </div>
        </div>
        
        <div style="display: flex; gap: 20px; align-items: center; margin-bottom: 30px; background: var(--bg-tertiary); padding: 20px; border-radius: 8px;">
            <div style="font-size: 48px;">🔀</div>
            <div>
                <h4 style="margin-bottom: 5px;">Conflict Resolution</h4>
                <p style="font-size: 14px; color: var(--text-secondary);">Built-in load order sorting (using LOOT) ensures your mods load in the correct sequence, preventing crashes and missing textures.</p>
            </div>
        </div>
        
        <button class="btn btn-primary btn-lg" style="width: 100%; max-width: 300px;">Download Vortex (v1.9.12)</button>
    """),
    ("api-docs", "API Docs", "Documentation for developers building with the ViierMods API.", """
        <h3 style="font-family:'Rajdhani'; font-size:24px; margin-bottom:12px;">Build With Us</h3>
        <p style="margin-bottom:16px; color:var(--text-secondary);">The ViierMods API allows developers to programmatically access mod data, user profiles, and download links. Whether you are building an external mod manager, a Discord bot, or a statistics tracker, our RESTful API provides the data you need.</p>
        
        <div style="background: #0d0f14; padding: 15px; border-radius: 6px; font-family: monospace; font-size: 13px; margin-bottom: 20px; border: 1px solid #333;">
            <span style="color: #4CAF50;">GET</span> /v1/games/{domain_name}/mods/{id}.json<br>
            <span style="color: #888;">// Returns metadata for a specific mod</span>
        </div>
        
        <p style="margin-bottom:16px; color:var(--text-secondary);">To get started, you will need to generate a Personal API Key from your account settings. All requests must include this key in the header: <code>apikey: YOUR_KEY_HERE</code>.</p>
        
        <a href="#" class="btn btn-ghost" style="display:inline-block;">Generate API Key</a>
    """),
    ("contact-us", "Contact Us", "Get in touch with the ViierMods team.", """
        <h3 style="font-family:'Rajdhani'; font-size:24px; margin-bottom:12px;">We're Here to Help</h3>
        <p style="margin-bottom:24px; color:var(--text-secondary);">If you couldn't find the answer to your question in our Help Center or Forums, you can reach out to our support staff directly by opening a ticket below.</p>
        
        <form style="display: flex; flex-direction: column; gap: 16px; max-width: 600px;">
            <div style="display: flex; gap: 16px;">
                <input type="text" placeholder="Your Name" class="form-input" style="flex:1; padding: 10px; border-radius: 4px; border: 1px solid var(--border-subtle); background: var(--bg-tertiary); color: white;">
                <input type="email" placeholder="Email Address" class="form-input" style="flex:1; padding: 10px; border-radius: 4px; border: 1px solid var(--border-subtle); background: var(--bg-tertiary); color: white;">
            </div>
            <select class="form-input" style="padding: 10px; border-radius: 4px; border: 1px solid var(--border-subtle); background: var(--bg-tertiary); color: white;">
                <option>Select a Category...</option>
                <option>Billing & Premium Support</option>
                <option>Account Recovery</option>
                <option>Report a User/Mod</option>
                <option>Business Inquiry</option>
            </select>
            <textarea placeholder="Describe your issue in detail..." rows="6" style="padding: 10px; border-radius: 4px; border: 1px solid var(--border-subtle); background: var(--bg-tertiary); color: white; resize: vertical;"></textarea>
            <button type="button" class="btn btn-primary" style="width: 150px;">Send Message</button>
        </form>
    """),
    ("donate", "Donate", "Support the platform and our mod authors.", """
        <h3 style="font-family:'Rajdhani'; font-size:24px; margin-bottom:12px;">Support Modding</h3>
        <p style="margin-bottom:16px; color:var(--text-secondary);">ViierMods is kept alive by the incredible generosity of our community. While buying Premium is the best way to get perks while supporting us, you can also make one-time donations to keep the servers running.</p>
        
        <div style="background: linear-gradient(135deg, rgba(217,143,64,0.1), transparent); border: 1px solid var(--accent-primary); border-radius: 8px; padding: 24px; margin-bottom: 24px; text-align: center;">
            <h4 style="margin-bottom: 10px; font-size: 20px; color: var(--accent-primary);">Mod Author Donation Fund (DP)</h4>
            <p style="font-size: 14px; color: var(--text-secondary); margin-bottom: 20px;">Did you know? Every month, we distribute a pool of money to mod authors based on how many unique downloads they receive via our Donation Points (DP) system. Your donation goes directly into this pool to pay creators!</p>
            <div style="display: flex; gap: 10px; justify-content: center; margin-bottom: 20px;">
                <button class="btn btn-ghost" style="border: 1px solid var(--border-subtle); width: 80px;">$5</button>
                <button class="btn btn-ghost" style="border: 1px solid var(--border-subtle); width: 80px;">$10</button>
                <button class="btn btn-primary" style="width: 80px;">$25</button>
                <button class="btn btn-ghost" style="border: 1px solid var(--border-subtle); width: 80px;">$50</button>
            </div>
            <button class="btn btn-primary btn-lg" style="width: 100%; max-width: 350px;">Donate via PayPal / Stripe</button>
        </div>
    """)
]

template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} - ViierMods</title>
  <link rel="stylesheet" href="/index.css" />
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%23d98f40'/%3E%3Ctext x='16' y='23' text-anchor='middle' font-family='Arial' font-weight='900' font-size='20' fill='%230d0f14'%3EV%3C/text%3E%3C/svg%3E" />
</head>
<body>
  <header class="main-header">
    <div class="header-inner">
      <a href="/" class="logo"><div class="logo-icon">V</div><div class="logo-text">VIIER<span>MODS</span></div></a>
      <nav class="main-nav">
        <a href="/" class="nav-link">Home</a>
        <a href="/games" class="nav-link">Games</a>
        <a href="/mods" class="nav-link">Mods</a>
        <a href="/community" class="nav-link">Community</a>
        <a href="/collections" class="nav-link">Collections</a>
        <a href="/news" class="nav-link">News</a>
      </nav>
      <div class="header-actions">
        <a href="/login" class="btn btn-ghost" style="border: none;">Log In</a>
        <a href="/signup" class="btn btn-primary">Register</a>
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
      <div style="font-size: 16px; color: var(--text-primary); line-height: 1.8;">
        {content}
      </div>
      <div style="margin-top: var(--space-2xl); padding-top: var(--space-xl); border-top: 1px solid var(--border-subtle);">
        <p style="color: var(--text-tertiary); font-size: 14px;">Last updated: September 2026</p>
      </div>
    </div>
  </main>

  <footer class="main-footer">
    <div class="container">
      <div class="footer-bottom" style="border:none;padding:0;">
        <p class="footer-copyright">© 2024 ViierMods. All rights reserved.</p>
        <div class="footer-legal">
          <a href="/privacy-policy">Privacy Policy</a>
          <a href="/terms-of-service">Terms of Service</a>
          <a href="/cookie-policy">Cookie Policy</a>
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
