from django.db import models


class ContactMessage(models.Model):
    """
    Model for storing contact form submissions from the landing page.
    Handles inquiries about services.
    """
    name = models.CharField(max_length=255)
    email = models.EmailField()
    company = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)

    SERVICE_CHOICES = [
        ('software', 'Software Architecture & Web Engineering'),
        ('cybersecurity', 'Cybersecurity & Threat Mitigation'),
        ('marketing', 'Performance Marketing & Brand Growth'),
        ('design', 'UI/UX & Brand Design'),
        ('full_stack', 'Full 360° Integration'),
        ('other', 'Other'),
    ]
    service = models.CharField(
        max_length=50,
        choices=SERVICE_CHOICES,
        default='other')
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"{self.name} - {self.company or 'No Company'} ({self.get_service_display()})"


class Service(models.Model):
    """
    Model for storing agency services dynamically.
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_name = models.CharField(
        max_length=100, help_text="Lucide icon name (e.g. 'code-2', 'shield-check')")
    color_theme = models.CharField(
        max_length=50, help_text="Tailwind color prefix (e.g. 'accent', 'success', 'orange-400', 'purple-400')")
    order = models.PositiveIntegerField(
        default=0, help_text="Order in which service appears")

    # Features/Bullet points could be a separate model, or stored as JSON, but for simplicity we will store them as a newline-separated string
    features = models.TextField(
        help_text="Enter features separated by a new line", blank=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title

    def get_features_list(self):
        return [f.strip() for f in self.features.split('\n') if f.strip()]


class TeamMember(models.Model):
    """
    Model for storing team members dynamically.
    """
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    department = models.CharField(
        max_length=100, help_text="e.g. 'Advanced Engineering', 'Defensive Architecture'")
    bio = models.TextField()
    image = models.ImageField(
        upload_to="team/", help_text="Upload 1:1 ratio square WebP image")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"

    def __str__(self):
        return self.name
