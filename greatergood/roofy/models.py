from django.db import models
from django.contrib.auth.models import User

MAIN_CONTACT_PREFIX_CHOICES = (
        ('Mr.', 'Mr.'),
        ('Mrs.', 'Mrs.'),
        ('Ms.','Ms.'),
        ('Dr.','Dr.')
    )
MAIN_CONTACT_TITLE = (
	  ('Builder','Builder'),
	  ('Buyer','Buyer'),
	  ('Caretaker','Caretaker'),
	  ('COO','COO'),
	  ('Daughter','Daughter'),
	  ('Husband','Husband'),
	  ('Manager','Manager'),
	  ('Owner','Owner'),
	  ('President','President'),
	  ('Realtor','Realtor'),
	  ('Seller','Seller'),
	  ('Son','Son'),
	  ('Tenant','Tenant'),
	  ('Trustee','Trustee'),
	  ('Vice-President','Vice-President'),
	  ('Wife','Wife'),
	)
ACCOUNT_TYPE_CHOICES = (
    ('Residential','Residential'),
    ('Business','Business')
	)

STATE_CHOICES = (
    ('Illinois','Illinois'),
    ('Indiana','Indiana'),
    ('Wisconsin','Wisconsin')
	)
SITE_TYPES = (
  ('4-Plex','4-Plex'),
  ('Agriculture/Range','Agriculture/Ranch'),
  ('Apartment Building','Apartment Building'),
  ('Apartment Complex','Apartment Complex'),
  ('Cabin','Cabin'),
  ('Commercial - Gas Station','Commercial - Gas Station'),
  ('Commercial - Hotel','Commercial - Hotel'),
  ('Commercial - Other','Commercial - Other'),
  ('Commercial - Church','Commercial - Church'),
  ('Commercial - Retail','Commercial - Retail'),
  ('Duplex','Duplex'),
  ('Garages/Shed','Garages/Shed'),
  ('Gazebo','Gazebo'),
  ('New Construction','New Construction'),
  ('Residential-Own','Residential-Own'),
  ('Residential-Rental','Residential-Rental'),
	)
LEAD_SOURCE_TYPES = (
	('Angies List','Angies List'),
	('BBB','BBB'),
	('Canvassing','Canvassing'),
	('Direct Mail','Direct Mail'),
	('Previous Customer','Previous Customer'),
	('Referral','Referral'),
	('Self Generated','Self Generated'),
	('Telemarketing Campaign','Telemarketing Campaign'),
	('Truck Decals','Truck Decals'),
	('Website','Website'),
	('Yard Sign','Yard Sign'),

	)
ROOF_TYPES = (
    ('Flat Roof','Flat Roof'),
    ('Steel Roof','Steel Roof'),
	('Wood Shake','Wood Shake'),
    ('3-Tab Shingles','3-Tab Shingles'),
    ('Architectural Shingles','Architectural Shingles'),
    ('Organic Shingles','Organic Shingles'),
    ('Slate Roof','Slate Roof'),
    ('Clay Tile Roof','Clay Tile Roof'),
	)
STORIES_TYPES = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),


	)

ELEVATION_TYPES = (
  ('Brick','Brick'),
  ('Asphalt','Asphalt'),
  ('Aluminum','Aluminum'),
  ('Vinyl','Vinyl'),
  ('Brick/Siding','Brick/Siding'),
  ('Hardwood','Hardwood'),
	)
ROOF_DAMAGE_TYPES = (
 ('Hail','Hail'),
 ('Hail+Mising Shingles','Hail+Missing Shingles'),
 ('Wind','Wind'),
 ('Wind+Missing Shingles','Wind+Missing Shingles'),
 ('Racoon','Racoon'),
 ('Racoon+Missing Shingles','Racoon+Missing Shingles'),
 ('Hail&Wind','Hail&Wind'),
 ('Hail&Wind+Missing Shingles','Hail&Wind+Missing Shingles'),
  	)


# Create your models here.
teeps = ()
user_list = my_choices = [

]
users = User.objects.all()
for x in users:
  user_list.append( (str(x),str(x)))
print(STATE_CHOICES)
USER_CHOICES = tuple(user_list)



class Client(models.Model):
  

  #Contact Info
  main_contact_prefix = models.CharField(max_length=200, choices=MAIN_CONTACT_PREFIX_CHOICES)
  main_contact_first_name = models.CharField(max_length=200)
  main_contact_last_name = models.CharField(max_length=200)
  main_contact_title = models.CharField(max_length=200,choices=MAIN_CONTACT_TITLE)
  main_contact_nick_name = models.CharField(max_length=200)
  main_contact_home_phone = models.CharField(max_length=200)
  main_contact_work_phone = models.CharField(max_length=200)
  main_contact_work_ext = models.CharField(max_length=200)
  main_contact_cell_phone = models.CharField(max_length=200)
  main_contact_fax_phone = models.CharField(max_length=200)
  main_contact_email = models.CharField(max_length=200)

  #Account Info
  account_type = models.CharField(max_length=200, choices=ACCOUNT_TYPE_CHOICES)
  mailing_address = models.CharField(max_length=200)
  city = models.CharField(max_length=200)
  state = models.CharField(max_length=200,choices=STATE_CHOICES)
  zipcode = models.CharField(max_length=200)
  #sales_rep = forms.ModelChoiceField(queryset=User.objects.all())
  sales_rep = models.CharField(max_length=200,choices=USER_CHOICES)
    #ClientComments
  comments = models.CharField(max_length=200)

  def __str__(self):
        return self.main_contact_first_name + " " + self.main_contact_last_name


class Project(models.Model):
  client = models.ForeignKey(Client, on_delete=models.CASCADE)
  project_name = models.CharField(max_length=200)
  sales_rep = models.CharField(max_length=200,choices=USER_CHOICES)
  site_address = models.CharField(max_length=200)
  city = models.CharField(max_length=200)
  state = models.CharField(max_length=200,choices=STATE_CHOICES)
  zipcode = models.CharField(max_length=200)
  site_notes = models.CharField(max_length=200)
  site_type = models.CharField(max_length=200,choices=SITE_TYPES)
  lead_source = models.CharField(max_length=200,choices=LEAD_SOURCE_TYPES)
  refered_by = models.CharField(max_length=200)
  storm_date = models.DateField()
  claim_number = models.CharField(max_length=200)
  policy_number = models.CharField(max_length=200)
  insurance_company = models.CharField(max_length=200)
  mortgage_company = models.CharField(max_length=200)
  roof_style = models.CharField(max_length=200,choices=ROOF_TYPES)
  steep = models.BooleanField()
  walk_on = models.BooleanField()
  how_many_stories = models.CharField(max_length=200,choices=STORIES_TYPES)
  elevation = models.CharField(max_length=200,choices=ELEVATION_TYPES)
  damage_on_roof = models.BooleanField()
  damage_on_siding = models.BooleanField()
  damage_on_gutters = models.BooleanField() 
  damage_on_downspouts = models.BooleanField()
  damage_on_window_wraps = models.BooleanField()
  damage_on_ac = models.BooleanField()
  type_of_roof_damage = models.CharField(max_length=200,choices=ROOF_DAMAGE_TYPES)
  how_many_layers = models.CharField(max_length=200)
  interior_damage = models.BooleanField()
  place_of_interior_damage = models.CharField(max_length=200)
  pets_we_should_be_aware_of = models.BooleanField()
  locked_gate = models.BooleanField()
  garage_attached = models.BooleanField()

  def __str__(self):
    return self.site_address
  