# Salad API Documentation

## `GET` paypal/users
`GET` the PayPal account of the authenticated user.

URL: https://app-api.salad.io/health/ready

Responses:
```json
No connected PayPal Account was found.
```

> Returns the authenticated user's PayPal account

In case if the user don't have a PayPal account or have link their PayPal account to Salad, the API will return `No connected PayPal Account was found.`

HTTP response status codes
200	- OK