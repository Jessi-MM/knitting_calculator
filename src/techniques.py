"""
Hi

"""
from body_measurements import BodyMeasurements
from tension_gauge import *

class ShortRows:
    def __init__(self, gauge_sts_per_cm, gauge_rows_per_cm):

        self.gauge_sts_per_cm = gauge_sts_per_cm
        self.gauge_rows_per_cm = gauge_rows_per_cm

    @classmethod
    def short_rows_given_lenght(self, lenght):
        short_rows = round(lenght * gauge_rows_per_cm)
        if short_rows % 2 != 0:  # If it's odd, round up to the next even number
            short_rows += 1
        return short_rows // 2
    

    
class RaglanSweater:
    def __init__(self, gauge_sts_per_cm, gauge_rows_per_cm, category, size, raglan_st, divisions=4):
        """
        Initialize the raglan sweater using gauge and body size.
        """
        self.gauge_sts_per_cm = gauge_sts_per_cm
        self.gauge_rows_per_cm = gauge_rows_per_cm

        # Get lenght of neck from BodyMeasurements
        body_measurements = BodyMeasurements.get_measurements(category, size)
        if body_measurements is None:
            raise ValueError("Invalid category or size")
        
        self.neck_circumference = (body_measurements["head"]+body_measurements["neck"])/2
        self.sproot = body_measurements["neck"]/6 - 2
        self.raglan_st = raglan_st  # Stitches of ranglan pattern
        self.divisions = divisions  # To get back, front and sleeves

    def calculate_cast_on(self):
        """
        Calculate how many stitches to cast on.
        """
        short_rows_sproot = ShortRows.short_rows_given_lenght(self.sproot)  # Number of short rows
        total_sts = round(self.neck_circumference * self.gauge_sts_per_cm)
        total_sts_to_divide = total_sts - self.divisions*self.raglan_st

        back_sts = round(0.3333333 * total_sts_to_divide - 2 * short_rows_sproot)
        front_sts = round(0.3333333 * total_sts_to_divide + 2 * short_rows_sproot)
        sleeve_sts = round((0.3333333 * total_sts_to_divide)/2)

        return {
            "total_stitches": total_sts,
            "short_rows_sproot": short_rows_sproot,
            "back": back_sts,
            "front": front_sts,
            "each_sleeve": sleeve_sts,
        }

# Example Usage
gauge_sts_per_cm, gauge_rows_per_cm = tension(gauge_width_cm=10, gauge_height_cm=10, gauge_sts=40, gauge_rows=27)
sweater = RaglanSweater(gauge_sts_per_cm, gauge_rows_per_cm, raglan_st=2, category="women", size="S")
stitch_distribution = sweater.calculate_cast_on()


print(f"Total stitches: {stitch_distribution['total_stitches']}")
print(f"Raglan stitches: {stitch_distribution['raglan_stitches']}")
print(f"Short rows to fit well: {stitch_distribution['short_rows_sproot']}")
print(f"Back: {stitch_distribution['back']}, Front: {stitch_distribution['front']}, Sleeves: {stitch_distribution['each_sleeve']}")

