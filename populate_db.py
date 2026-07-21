from core.models import Service, TeamMember
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()


def populate():
    # Populate Services
    services = [
        {
            "title": "Software Architecture & Web Engineering",
            "description": "Custom applications and infrastructure engineered to scale, not just to launch.",
            "icon_name": "code-2",
            "color_theme": "accent",
            "order": 1,
            "features": "Custom web & enterprise apps\nDjango & Laravel architecture\nAPI integrations & DB Design"
        },
        {
            "title": "Cybersecurity & Threat Mitigation",
            "description": "Security engineered in from day one — not audited in after launch.",
            "icon_name": "shield-check",
            "color_theme": "success",
            "order": 2,
            "features": "Penetration testing & ethical hacking\nVulnerability assessments\nInfrastructure hardening"
        },
        {
            "title": "Performance Marketing & Brand Growth",
            "description": "Growth engineered on real data, not assumptions.",
            "icon_name": "trending-up",
            "color_theme": "orange-400",
            "order": 3,
            "features": "Lead generation & campaigns\nContent strategy & funnels\nBrand positioning"
        },
        {
            "title": "UI/UX & Brand Design",
            "description": "Design that is engineered for conversion and trust, not just aesthetics.",
            "icon_name": "palette",
            "color_theme": "purple-400",
            "order": 4,
            "features": "Brand identity systems\nWeb interface design (UI/UX)\nSocial & campaign assets"
        }
    ]

    for svc in services:
        Service.objects.get_or_create(title=svc['title'], defaults=svc)

    print("Services populated!")

    # Populate Team Members
    import shutil

    media_team_dir = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'media', 'team')
    static_team_dir = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'static', 'images', 'team')

    os.makedirs(media_team_dir, exist_ok=True)

    team = [
        ("Nabid Ahmad", "Full-Stack Developer", "Advanced Engineering",
         "Nabid works across Python/Django and PHP/Laravel, with hands-on project experience spanning school management systems, pharmacy management platforms, and fitness-club web applications.", "nabid.webp", 1),
        ("Md Shariful Islam Rony", "Full-Stack Developer", "Advanced Engineering",
         "Rony is a Python/Django developer who has architected and deployed three live full-stack applications, including a flight-booking platform integrating Google OAuth 2.0 and PostgreSQL.", "rony.webp", 2),
        ("Md Khairul Islam Akaid", "Cybersecurity Professional", "Defensive Architecture",
         "Khairul brings a Linux-first foundation to the team's security practice, with a growing specialization in cybersecurity fundamentals, threat awareness, and security operations tooling.", "khairul.webp", 3),
        ("Abdullah Al Siddik", "Cybersecurity Professional", "Defensive Architecture",
         "Abdullah focuses on offensive and defensive security — penetration testing, vulnerability assessment, and network monitoring. He applies OWASP Top 10 methodology to every web application the team ships.", "abdullah.webp", 4),
        ("Farzana Akter Popi", "Growth Specialist", "Growth & Performance",
         "Farzana leads client-facing marketing and lead generation. Her background spans digital marketing, CRM, and direct sales across several customer-facing roles.", "farzana.webp", 5),
        ("Afia Najnine", "Client Relations Specialist", "Growth & Performance",
         "Afia brings a client-facing foundation to the growth team, currently managing student communications, Meta Business Suite, and WhatsApp broadcast campaigns.", "afia.webp", 6),
        ("Nurul Ahanaf Adil", "Graphic Designer", "Visual Identity",
         "Nurul is an NSDA-certified graphic designer working across Adobe Photoshop and Illustrator to deliver social content, banners, and brand collateral.", "nurul.webp", 7)
    ]

    for name, designation, dept, bio, img_name, order in team:
        src = os.path.join(static_team_dir, img_name)
        dst = os.path.join(media_team_dir, img_name)
        if os.path.exists(src) and not os.path.exists(dst):
            shutil.copy(src, dst)

        TeamMember.objects.get_or_create(
            name=name,
            defaults={
                "designation": designation,
                "department": dept,
                "bio": bio,
                "image": f"team/{img_name}",
                "order": order
            }
        )
    print("Team populated!")


if __name__ == '__main__':
    populate()
