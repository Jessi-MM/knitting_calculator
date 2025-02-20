
class RaglanSweater:
    def __init__(self, gauge_width_cm, gauge_height_cm, gauge_sts, gauge_rows, category, size):
        """Initialize the raglan sweater using gauge and body size."""
        self.gauge_sts_per_cm = gauge_sts / gauge_width_cm
        self.gauge_rows_per_cm = gauge_rows / gauge_height_cm

        # Get chest size from BodyMeasurements
        body_measurements = BodyMeasurements.get_measurements(category, size)
        if body_measurements is None:
            raise ValueError("Invalid category or size")
        
        self.chest_circumference = body_measurements["chest"]

    def calculate_cast_on(self):
        """Calculate how many stitches to cast on."""
        total_sts = round(self.chest_circumference * self.gauge_sts_per_cm)

        back_sts = round(0.35 * total_sts)
        front_sts = round(0.35 * total_sts)
        sleeve_sts = round(0.15 * total_sts)

        return {
            "total_stitches": total_sts,
            "back": back_sts,
            "front": front_sts,
            "each_sleeve": sleeve_sts
        }

# Example Usage
sweater = RaglanSweater(gauge_width_cm=8, gauge_height_cm=10, gauge_sts=20, gauge_rows=16, category="women", size="M")
stitch_distribution = sweater.calculate_cast_on()

print(f"Total stitches: {stitch_distribution['total_stitches']}")
print(f"Back: {stitch_distribution['back']}, Front: {stitch_distribution['front']}, Sleeves: {stitch_distribution['each_sleeve']}")