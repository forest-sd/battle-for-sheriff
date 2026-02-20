#!/usr/bin/env python3
"""Generate static site for battle-for-sheriff.com — Bold red/charcoal gaming theme"""
import os, json

DOMAIN = "battle-for-sheriff.com"
PAGES_URL = "battle-for-sheriff.pages.dev"
SITE_NAME = "Battle for Sheriff"
TAGLINE = "Elect Your Hero in the Ultimate Showdown"

img_dir = "images"
all_images = sorted([f for f in os.listdir(img_dir) if f.endswith('.webp')])

posts = [
    {"slug": "discover-the-exciting-world-of-battle-for-sheriff-game", "title": "Discover the Exciting World of Battle for Sheriff Game", "date": "2024-11-30", "excerpt": "Dive into the world of Battle for Sheriff, where strategy meets adventure in an epic quest for power."},
    {"slug": "exciting-adventure-games-with-updates-you-must-try", "title": "Exciting Adventure Games With Updates You Must Try", "date": "2024-11-30", "excerpt": "Adventure games with regular updates keep content fresh and boost the gaming experience."},
    {"slug": "experience-exciting-fun-play-battle-for-sheriff-online", "title": "Experience Exciting Fun: Play Battle for Sheriff Online", "date": "2024-11-30", "excerpt": "Play Battle For Sheriff Online for an exhilarating experience filled with strategy and epic battles."},
    {"slug": "experience-the-ultimate-sheriff-showdown-the-best-strategies", "title": "Experience the Ultimate Sheriff Showdown: The Best Strategies", "date": "2024-11-30", "excerpt": "Master the best strategies to dominate in the ultimate sheriff showdown."},
    {"slug": "explore-the-exciting-world-of-hero-based-online-games", "title": "Explore the Exciting World of Hero-Based Online Games", "date": "2024-11-30", "excerpt": "Hero-based online games offer unique abilities, team dynamics, and strategic depth."},
    {"slug": "exploring-the-best-multiplayer-hero-strategy-games", "title": "Exploring the Best Multiplayer Hero Strategy Games", "date": "2024-11-30", "excerpt": "Multiplayer Hero Strategy Games offer an exhilarating blend of tactical gameplay and hero-based mechanics."},
    {"slug": "top-competitive-multiplayer-adventure-games-to-play-now", "title": "Top Competitive Multiplayer Adventure Games to Play Now", "date": "2024-11-30", "excerpt": "Discover the best competitive multiplayer adventure games that combine teamwork and strategy."},
    {"slug": "top-online-strategy-games-to-watch-in-2025", "title": "Top Online Strategy Games to Watch in 2025", "date": "2025-08-19", "excerpt": "The best online strategy games coming in 2025 that every gamer should keep on their radar."},
    {"slug": "top-sheriff-role-playing-games-you-must-try-today", "title": "Top Sheriff Role-Playing Games You Must Try Today", "date": "2024-11-30", "excerpt": "The best Sheriff RPGs combine thrilling narratives with characters embodying authority and justice."},
    {"slug": "top-strategy-games-for-teamwork-and-collaboration", "title": "Top Strategy Games for Teamwork and Collaboration", "date": "2024-11-30", "excerpt": "Strategy games for teamwork encourage collaboration, communication, and strategic thinking."},
]

NAV = [("Home", "/"), ("About", "/about/"), ("Contact", "/contact-us/")]

def header(title, desc="", canonical="/"):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc or title}">
<link rel="canonical" href="https://{PAGES_URL}{canonical}">
<link rel="icon" href="/images/favicon.png">
<link rel="stylesheet" href="/css/style.css">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc or title}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://{PAGES_URL}{canonical}">
</head>
<body>
<header class="header">
  <div class="header__inner">
    <a href="/" class="header__logo">⚔️ {SITE_NAME}</a>
    <nav class="header__nav">
      <button class="menu-toggle" aria-label="Menu">&#9776;</button>
      <ul class="nav__list">
        {''.join(f'<li><a href="{url}">{name}</a></li>' for name, url in NAV)}
      </ul>
    </nav>
  </div>
</header>
'''

FOOTER = f'''
<footer class="footer">
  <div class="footer__inner">
    <div class="footer__col">
      <h3>⚔️ {SITE_NAME}</h3>
      <p>{TAGLINE}. Join our vibrant community of players passionate about strategy games and interactive storytelling.</p>
    </div>
    <div class="footer__col">
      <h3>Quick Links</h3>
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/about/">About</a></li>
        <li><a href="/contact-us/">Contact</a></li>
        <li><a href="/privacy/">Privacy</a></li>
        <li><a href="/terms/">Terms</a></li>
      </ul>
    </div>
  </div>
  <div class="footer__bottom">
    <p>&copy; 2024 {SITE_NAME}. All rights reserved.</p>
  </div>
</footer>
<script>
document.querySelector('.menu-toggle').addEventListener('click', function() {{
  document.querySelector('.nav__list').classList.toggle('active');
}});
</script>
</body>
</html>'''

def post_card(post, idx):
    img = all_images[idx % len(all_images)] if all_images else ""
    return f'''<article class="card">
  <a href="/posts/{post['slug']}/">
    {f'<img src="/images/{img}" alt="{post["title"]}" class="card__img" loading="lazy">' if img else ''}
    <div class="card__body">
      <h2 class="card__title">{post['title']}</h2>
      <time class="card__date">{post['date']}</time>
      <p class="card__excerpt">{post['excerpt']}</p>
    </div>
  </a>
</article>'''

def write(path, content):
    os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)

# Homepage
home_schema = json.dumps({"@context":"https://schema.org","@type":"WebSite","name":SITE_NAME,"url":f"https://{PAGES_URL}/","description":TAGLINE}, indent=2)
home = header(f"{SITE_NAME} — {TAGLINE}", TAGLINE, "/")
home += f'<script type="application/ld+json">{home_schema}</script>\n'
home += '<main class="main">\n<section class="hero">\n'
home += f'<h1>{SITE_NAME}</h1>\n<p class="hero__tagline">{TAGLINE}</p>\n'
home += '<p>Welcome to Battle for Sheriff, where adventure and strategy collide in an exhilarating quest to reclaim power! Here, we invite you to become a part of our vibrant community of players who are passionate about strategy games and interactive storytelling.</p>\n'
home += '<p>At Battle for Sheriff, our mission is clear: to provide an engaging platform where players can collaborate, compete, and immerse themselves in captivating gameplay. Whether you\'re strategizing with friends or challenging opponents, every game is designed to test your skills and wit.</p>\n'
home += '<div class="hero__features"><div class="feature">🎮 Engaging Gameplay</div><div class="feature">🏆 Competitive Edge</div><div class="feature">👥 Community Events</div><div class="feature">🔄 Continuous Updates</div></div>\n'
home += '</section>\n'
home += '<section class="posts-grid">\n<h2>Latest Articles</h2>\n<div class="grid">\n'
for i, p in enumerate(posts[:6]):
    home += post_card(p, i)
home += '</div>\n</section>\n</main>\n'
home += FOOTER
write("index.html", home)

# About
about = header("About Battle for Sheriff", "Learn about Battle for Sheriff and our gaming community.", "/about/")
about += '''<main class="main"><article class="page">
<h1>About Battle for Sheriff</h1>
<p>Battle for Sheriff is an exciting strategy game platform where players compete in thrilling showdowns to become the ultimate sheriff. Our game combines elements of tactical strategy, hero-based mechanics, and interactive storytelling to create an unforgettable gaming experience.</p>
<h2>Our Mission</h2>
<p>Our mission is to provide an engaging platform where players can collaborate, compete, and immerse themselves in captivating gameplay. We believe that great games bring people together, and Battle for Sheriff is designed to foster community, competition, and camaraderie among players from around the world.</p>
<h2>Gameplay Features</h2>
<p>Battle for Sheriff offers a rich gaming experience with multiple game modes, customizable heroes, and strategic depth that rewards both newcomers and veteran players. Our unique hero system allows players to choose from a diverse roster of characters, each with their own abilities and playstyles. Whether you prefer defensive strategies, aggressive tactics, or support roles, there's a hero that matches your preferred way to play.</p>
<h2>Community First</h2>
<p>We pride ourselves on our active and welcoming community. Regular events, tournaments, and community challenges keep the gameplay fresh and exciting. Our forums and social channels provide spaces for players to share strategies, form teams, and connect with fellow gaming enthusiasts.</p>
<h2>Continuous Development</h2>
<p>Our dedicated development team works tirelessly to improve and expand the game. Regular updates introduce new heroes, maps, game modes, and features based on community feedback. We believe that a great game is never finished — it evolves with its players.</p>
</article></main>
''' + FOOTER
write("about/index.html", about)

# Contact
contact = header("Contact Us — Battle for Sheriff", "Get in touch with the Battle for Sheriff team.", "/contact-us/")
contact += '''<main class="main"><article class="page">
<h1>Contact Us</h1>
<p>Have questions, feedback, or suggestions? We'd love to hear from you! The Battle for Sheriff team is always looking to improve the gaming experience for our community.</p>
<div class="contact-info">
<h2>Get in Touch</h2>
<ul>
<li><strong>Email:</strong> support@battle-for-sheriff.com</li>
<li><strong>Community Forums:</strong> Join our player community</li>
</ul>
</div>
<h2>Report Issues</h2>
<p>Encountered a bug or technical issue? Please reach out to our support team with details about the problem, including your device, browser, and steps to reproduce the issue. We take all reports seriously and work quickly to resolve them.</p>
<h2>Partnership Inquiries</h2>
<p>Interested in partnering with Battle for Sheriff? Whether you're a content creator, esports organizer, or gaming community leader, we're open to collaboration. Contact us to discuss partnership opportunities.</p>
<h2>Stay Connected</h2>
<p>Follow us on social media to stay up to date with the latest news, updates, events, and community highlights. Join our growing community of strategy gaming enthusiasts!</p>
</article></main>
''' + FOOTER
write("contact-us/index.html", contact)

# Privacy
privacy = header("Privacy Policy — Battle for Sheriff", "Battle for Sheriff privacy policy.", "/privacy/")
privacy += '''<main class="main"><article class="page">
<h1>Privacy Policy</h1>
<p>At Battle for Sheriff, we respect your privacy. This policy outlines how we collect, use, and protect your information.</p>
<h2>Information We Collect</h2>
<p>We may collect information you provide when creating an account, participating in forums, or contacting support. This includes your username, email address, and gameplay data.</p>
<h2>How We Use Your Information</h2>
<p>We use collected information to provide and improve our gaming services, communicate updates and events, ensure fair play, and personalize your experience.</p>
<h2>Data Protection</h2>
<p>We implement industry-standard security measures to protect your data. We do not sell your personal information to third parties.</p>
<h2>Contact</h2>
<p>Questions about this policy? Contact us at support@battle-for-sheriff.com.</p>
</article></main>
''' + FOOTER
write("privacy/index.html", privacy)

# Terms
terms = header("Terms of Service — Battle for Sheriff", "Battle for Sheriff terms of service.", "/terms/")
terms += '''<main class="main"><article class="page">
<h1>Terms of Service</h1>
<p>By using Battle for Sheriff, you agree to these terms. Please read them carefully.</p>
<h2>1. Account Responsibility</h2>
<p>You are responsible for maintaining the security of your account. Do not share your login credentials with others.</p>
<h2>2. Fair Play</h2>
<p>We expect all players to engage in fair play. Cheating, exploiting bugs, or using unauthorized software may result in account suspension or termination.</p>
<h2>3. Community Guidelines</h2>
<p>Respectful behavior is expected in all community interactions. Harassment, hate speech, and toxic behavior will not be tolerated.</p>
<h2>4. Intellectual Property</h2>
<p>All game content, including graphics, text, and gameplay mechanics, is the property of Battle for Sheriff and protected by copyright law.</p>
<h2>5. Contact</h2>
<p>Questions about these terms? Contact support@battle-for-sheriff.com.</p>
</article></main>
''' + FOOTER
write("terms/index.html", terms)

# Posts
generic_gaming = """<h2>The World of Strategy Gaming</h2>
<p>Strategy games have evolved dramatically over the years, growing from simple board game adaptations to complex, multiplayer experiences that challenge players to think critically, plan ahead, and adapt to ever-changing situations. The genre continues to attract millions of players worldwide who appreciate the intellectual challenge and social dynamics that these games offer.</p>
<h2>What Makes a Great Strategy Game</h2>
<p>The best strategy games share several key elements: deep gameplay mechanics that reward mastery, balanced competition that keeps matches exciting, meaningful choices that impact outcomes, and a community of engaged players who push each other to improve. Whether you prefer real-time strategy, turn-based tactics, or hero-based team games, the genre offers something for every type of gamer.</p>
<h2>The Rise of Hero-Based Strategy</h2>
<p>One of the most exciting developments in strategy gaming is the rise of hero-based mechanics. Games that allow players to choose unique characters with distinct abilities add a layer of personalization and depth to the strategic experience. Team composition becomes as important as individual skill, creating a rich metagame that evolves with each update and patch.</p>
<h2>Building Community Through Competition</h2>
<p>Competitive gaming has become a powerful force for building communities. Tournaments, leagues, and ranked play systems give players goals to strive for, while forums, streams, and social media create spaces for sharing knowledge and connecting with fellow enthusiasts. The social aspect of strategy gaming is often just as rewarding as the gameplay itself.</p>
<h2>Looking Ahead</h2>
<p>The future of strategy gaming is bright, with advances in AI, networking technology, and game design pushing the boundaries of what's possible. From cross-platform play to AI-powered opponents that adapt to your playstyle, the next generation of strategy games promises to be more immersive, accessible, and engaging than ever before.</p>"""

for i, post in enumerate(posts):
    img = all_images[i % len(all_images)] if all_images else ""
    schema = json.dumps({"@context":"https://schema.org","@type":"Article","headline":post['title'],"datePublished":post['date'],"publisher":{"@type":"Organization","name":SITE_NAME}}, indent=2)
    
    related = [p for p in posts if p['slug'] != post['slug']][:3]
    related_html = '<div class="related"><h2>More Articles</h2><div class="related__grid">'
    for r in related:
        related_html += f'<a href="/posts/{r["slug"]}/" class="related__item"><h3>{r["title"]}</h3><time>{r["date"]}</time></a>'
    related_html += '</div></div>'
    
    page = header(post['title'], post['excerpt'], f"/posts/{post['slug']}/")
    page += f'<script type="application/ld+json">{schema}</script>\n'
    page += f'<main class="main"><article class="post">\n'
    page += f'<h1>{post["title"]}</h1>\n<time class="post__date">{post["date"]}</time>\n'
    if img:
        page += f'<img src="/images/{img}" alt="{post["title"]}" class="post__img" loading="lazy">\n'
    page += f'<div class="content">{generic_gaming}</div>\n'
    page += related_html
    page += '</article></main>\n'
    page += FOOTER
    write(f"posts/{post['slug']}/index.html", page)

# Sitemap
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
urls = ["/", "/about/", "/contact-us/", "/privacy/", "/terms/"]
urls += [f"/posts/{p['slug']}/" for p in posts]
for u in urls:
    sitemap += f'  <url><loc>https://{PAGES_URL}{u}</loc></url>\n'
sitemap += '</urlset>'
write("sitemap.xml", sitemap)

write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: https://{PAGES_URL}/sitemap.xml\n")

print(f"Generated {len(urls)} pages for {SITE_NAME}")
