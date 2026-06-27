from django.db import models

# Create your models here.
class EventList(models.Model):

    class EventCategory(models.TextChoices):
        CONFERENCE = 'CONFERENCE','Conference'
        PARTY = 'PARTY','Party'
        WEDDING = 'WEDDING','Wedding'
        SEMINAR = 'SEMINAR','Seminar'
        OTHER = 'OTHER','Other'
    class EventMode(models.TextChoices):
        ONLINE = 'ONLINE','Online'
        IN_PERSON = 'IN-PERSON','In-Person'
        BOTH = 'BOTH','Both'
    class EventPaymentCurrency(models.TextChoices):
        GHC = 'GHC','Ghc'
        RAND = 'RAND','Rand'
        USD = 'USD','Dollar'
        EUR = 'EUR','Euro'
        GBP = 'GBP','Pound'
    class EventStatus(models.TextChoices):
        UPCOMING = 'UPCOMING','Upcoming'
        ONGOING = 'ONGOING','Ongoing'
        ENDED = 'ENDED','Ended'

    ### FIELDS FOR EVENT LIST
    event_id = models.CharField(max_length=10,
                          unique=True,
                          editable=False,
                          blank=True
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(upload_to='event/thumbnail',null=True,blank=True)
    category = models.CharField(
        max_length=10,
        choices=EventCategory.choices,
        default=EventCategory.CONFERENCE
    )
    start_date = models.DateField()
    end_date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    mode = models.CharField(
        max_length=10,
        choices=EventMode.choices,
        default=EventMode.ONLINE
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00
    )
    currency = models.CharField(
        max_length=10,
        choices=EventPaymentCurrency.choices,default=EventPaymentCurrency.GHC,
        blank=True,
        null=True
    )
    status = models.CharField(
        max_length=10,
        choices=EventStatus.choices,
        default=EventStatus.UPCOMING
    )
    registration_open = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self,*args,**kwargs):
        new = self.pk is None
        super().save(*args,**kwargs)

        if new and not self.event_id:
            self.event_id = f"EVT-{self.pk:03d}"
            EventList.objects.filter(pk=self.pk).update(event_id=self.event_id)

    def __str__(self):
        return f"{self.event_id}--{self.title}"
    
    @property
    def free_event(self):
        if self.price == 0:
            return True
        else:
            return False



### SUB - FIELDS FOR EVENT DETAILS
class EventGallery(models.Model):
    event = models.ForeignKey(
        "EventDetail",
        on_delete=models.CASCADE,
        related_name="gallery",
        null=True,
        blank=True
    )
    image = models.ImageField(upload_to='event/gallery',null=True,blank=True)

    def __str__(self):
        return self.image.name.split('/')[-1] if self.image else "No Image"

class EventOrganizer(models.Model):
    event = models.OneToOneField(
        "EventDetail",
        on_delete=models.CASCADE,
        related_name="organizer",
        null=True,
        blank=True
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    website = models.URLField()

    def __str__(self):
        return str(self.name)

class EventVenue(models.Model):
    event = models.OneToOneField(
        "EventDetail",
        on_delete=models.CASCADE,
        related_name="venue",
        null=True,
        blank=True
    )
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9,decimal_places=6)
    longitude = models.DecimalField(max_digits=9,decimal_places=6)

    def __str__(self):
        return f"{self.name}--{self.address}"

class EventSpeakers(models.Model):
    event = models.ForeignKey(
        "EventDetail",
        on_delete=models.CASCADE,
        related_name="speakers",
        null=True,
        blank=True
    )
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='event/speakers',null=True,blank=True)

    def __str__(self):
        return f"{self.name}--{self.title}"

class EventAgenda(models.Model):
    event = models.ForeignKey(
        "EventDetail",
        on_delete=models.CASCADE,
        related_name="agenda",
        null=True,
        blank=True
    )
    day = models.IntegerField()
    title = models.CharField(max_length=100)
    time = models.TimeField()

    def __str__(self):
        return f"{self.day}--{self.title}"

### MAIN EVENT DETAILS
class EventDetail(models.Model):
    event = models.OneToOneField(
        EventList,
        on_delete=models.CASCADE,
        related_name="detail"
    )

    description = models.TextField()

    capacity = models.PositiveIntegerField(default=0)
    registered = models.PositiveIntegerField(default=0)

    # tags can stay M2M (shared across events)
    tags = models.JSONField(default=list,null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def available_slots(self):
        return self.capacity - self.registered

    def __str__(self):
        return f"{self.event.title}"