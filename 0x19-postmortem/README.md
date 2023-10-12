# 0x19. Postmortem

# WebStack Debbugging 3 PostMortem

## Issue Summary

The issue involves a server Error. The server returns a 500 error when queried
This caused outage leading to no access of server content.

## Timeline

Start Time: October 9, 2023, 06:00(EAT)

End Time: October 11, 2023, 23:09(EAT)

The server was completly inaccessible during this time

## Root Cause and Resolution

The root cause of the problem in the system was caused by a typographical error.
The text in the file /var/www/html/wp-settings.php was written wrongly.
"class-wp-locale.phpp" This was the typographical error

The resolution was to:
- Check for any other typos in the code
- Ensure that all files are tested correctly.


## Corrective and Preventive measurers

To correct the error the typo was changed using a puppet script below

```
exec { 'wsd3':
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/' /var/www/html/wp-settings.php",
  path    =>  ['/bin', '/usr/bin']
}
```

This corrected the typo error and the connection to the server was successfull

To prevent this in future, the following preventive measures should be implemented

- Code Review and Testing: This ensures that typos and errors in code are corrected
before the become part of production environment
- Coding Standards: Coding standards should be enforced to ensure consistency.
- Test Driven Development: This could help detect problems before they are catastrophic.
