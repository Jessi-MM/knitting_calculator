
def tension(gauge_width_cm, gauge_height_cm, gauge_sts, gauge_rows):

    gauge_sts_per_cm = gauge_sts / gauge_width_cm
    gauge_rows_per_cm = gauge_rows / gauge_height_cm

    return gauge_sts_per_cm, gauge_rows_per_cm