def alarm_clock(day, vacation):
  """
  Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a 
  boolean indicating if we are on vacation, return a string of the form "7:00" 
  indicating when the alarm clock should ring. Weekdays, the alarm should be 
  "7:00" and on the weekend it should be "10:00". Unless we are on vacation --
  then on weekdays it should be "10:00" and weekends it should be "off". 
  """
  week_preset = "7:00" if not vacation else "10:00"
  weekend_preset = "10:00" if not vacation else "off"
  return week_preset if day not in [6,0] else weekend_preset
