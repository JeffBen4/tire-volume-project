def wind_chill(temperature, wind_speed):
    chill_factor = 35.74 \
    + 0.6215 * temperature \
    - 35.75 * wind_speed**0.16 \
    + 0.4275 * temperature * wind_speed**0.16
    rounded = round(chill_factor, 1)
    return rounded

def cels_from_fahr(fahr):
  """Convert a temperature in Fahrenheit to
  Celsius and return the Celsius temperature.
  """
  cels = (fahr - 32) * 5 / 9
  return cels