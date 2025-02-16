class BodyMeasurements:
    """
    Stores standard body measurements for different categories
    """

    standard_measurements = {
        "women": {
            "XS": {"chest": 80, "waist": 64, "hips": 88},
            "S": {"chest": 88, "waist": 72, "hips": 96},
            "M": {"chest": 96, "waist": 80, "hips": 104},
            "L": {"chest": 104, "waist": 88, "hips": 112},
        },
        "baby": {
            "3-6 months": {"chest": 44, "waist": 43, "hips": 46},
            "6-12 months": {"chest": 47, "waist": 46, "hips": 49},
        },
    }

    @classmethod
    def get_measurements(cls, category, size):
        """
        Retrieve measurements for a given category (women, babies) and size
        """
        return cls.standard_measurements.get(category, {}).get(size, None)
    
# Example usage
women_medium = BodyMeasurements.get_measurements("baby", "3-6 months")
print(f"Women M Chest: {women_medium['chest']} cm")