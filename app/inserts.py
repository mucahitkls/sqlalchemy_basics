from datetime import date
from models import *
from app.database import LocalSession, engine, Base

# 2 - generate database schema
Base.metadata.create_all(engine)

# 3 - create a new session
session = LocalSession()

# 4 - create movies
lotr = Movie('Lord Of the Rings', date(2001, 1,1))
last_samurai = Movie("Last Samurai", date(2003, 4, 2))
mission_impo = Movie("Mission Impossible", date(1996, 8, 23))

# 5 - create actors
orlando_bloom = Actor('Orlando Bloom', date(1977, 1, 13))
tom_cruise = Actor('Tom cruise', date(1962, 7, 3))
ving_rhames = Actor('Ving Rhames', date(1959, 5, 12))

# 6 - add actors to movies
lotr.actors = [orlando_bloom]
last_samurai.actors = [tom_cruise]
mission_impo.actors = [tom_cruise, ving_rhames]

# 7 - add contact details to actors
orlando_contact = ContactDetails("415 555 2671", "Burbank, CA", orlando_bloom)
tom_contact = ContactDetails("423 555 5623", "Glendale, CA", tom_cruise)
tom_contact_2 = ContactDetails("421 444 2323", "West Hollywood, CA", tom_cruise)
ving_contact = ContactDetails("421 333 9428", "Glendale, CA", ving_rhames)

# 8 - create stuntmen
orlando_stuntman = Stuntman("John Doe", True, orlando_bloom)
tom_stuntman = Stuntman("John Roe", True, tom_cruise)
ving_stuntman = Stuntman("Richard Roe", True, ving_rhames)

# 9 - persists data
session.add(lotr)
session.add(last_samurai)
session.add(mission_impo)

session.add(orlando_contact)
session.add(tom_contact)
session.add(tom_contact_2)
session.add(ving_contact)

session.add(orlando_stuntman)
session.add(tom_stuntman)
session.add(ving_stuntman)

# 10 - commit and close session
session.commit()
session.close()