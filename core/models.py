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
        return f"{
            self.name} - {
            self.company or 'No Company'} ({
            self.get_service_display()})"
