class BodyMeasurements:
    """
    Stores standard body measurements for different categories and allows custom measurements
    """

    # Standard sizes
    standard_measurements = {
        "women": {
            "S": {"head": 55, "neck":30, "chest": 84, "waist": 64, "armhole": 20},
        },
        "baby": {
            "0-3 months": {"neck": 19, "chest": 44, "armhole": 8, "armhole_body": 15, "armhole_sleeve": 14, "wrist": 10},
        },
    }

    # Custom user-defined measurements 
    custom_measurements = {}

    @classmethod
    def get_measurements(cls, category, size):
        """
        Retrieve measurements for a given category and size, checking both standard and custom
        """
        # Check standard measurements first
        if category in cls.standard_measurements and size in cls.standard_measurements[category]:
            return cls.standard_measurements[category][size]
        
        # Check custom measurements
        return cls.custom_measurements.get(category, {}).get(size, None)

    @classmethod
    def add_custom_measurements(cls, category, size, chest, waist, hips):
        """
        Allows users to add their own custom measurements
        """
        if category not in cls.custom_measurements:
            cls.custom_measurements[category] = {}  # Initialize category if not present
        
        cls.custom_measurements[category][size] = {"chest": chest, "waist": waist, "hips": hips}
        print(f"Custom measurement added for {category} - {size}!")


# Add a custom measurement
#BodyMeasurements.add_custom_measurements("women", "CustomSize", chest=92, waist=86, hips=102)

# Retrieve the custom measurement
#custom_size = BodyMeasurements.get_measurements("women", "CustomSize")
#print(f"Custom Women Size Chest: {custom_size['chest']} cm")
