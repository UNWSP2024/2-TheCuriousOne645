START
  PROMPT "Enter the person's age:"
  INPUT age
  
  IF age <= 1 THEN
    DISPLAY "The person is an infant."
  ELSE IF age > 1 AND age < 13 THEN
    DISPLAY "The person is a child."
  ELSE IF age >= 13 AND age < 20 THEN
    DISPLAY "The person is a teenager."
  ELSE
    DISPLAY "The person is an adult."
  ENDIF
END
