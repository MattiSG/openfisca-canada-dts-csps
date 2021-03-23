from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person

class calculate_overtime__averaged(Variable):
    value_type = float
    entity = Person
    label = u"Calculate the overtime for the averaging schedule scenario"
    definition_period = DAY
    reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html"

    def formula(persons, period, parameters):
      ot_hours = persons("calculate_overtime__total_clc_hours", period) - (persons("calculate_overtime__number_of_averaging_scheduled_clc_weeks", period) * persons("weekly_clc_standard_hours_of_work", period))
      return max_(0, ot_hours)

class calculate_overtime__total_clc_hours(Variable):
    value_type = float
    entity = Person
    label = u"Total hours in the averaging schedule"
    definition_period = DAY
    reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html"

class calculate_overtime__number_of_averaging_scheduled_clc_weeks(Variable):
    value_type = float
    entity = Person
    label = u"total number of weeks in the averaging schedule"
    definition_period = DAY
    reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html"