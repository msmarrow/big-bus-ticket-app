# Big Bus Ticket Stand

<img width="600px" src="https://d12dkjq56sjcos.cloudfront.net/pub/media/wysiwyg/chicago/13-about-usp-info-other-general/Tourists-On-Big-Bus-Tour-Chicago-Tour-Big-Bus-Tours_13-01-17.jpg">


In this scenario, you will build an application for
a the on-street sales staff at a _Big Bus_ location.

Customers arrive at a corner and expect to be
able to perform the following transactions with the salesperson:

* Buy tickets for an all-day pass up to 10 days in advance
* Get a refund for a ticket that was sold for a future date (i.e. not today)

Therefore, a ticket agent needs to:

* Sell tickets for any bus route, for today or for any date up to 10 days from now
* Issue refunds for future tickets
* Generate a report of the number of tickets sold today for a given route
* Generate a report of the total number of tickets sold on any given date (for all routes)

Business Rules:

* Every ticket must have a unique identifier on it.
* Up to 4 tickets can be purchased at once.
* Each bus has 89 seats.
* There are three routes: Red, Green, and Blue.
  * The Red route has 5 buses.
  * The Green route has 4 buses.
  * The Blue route has 2 buses.
* Tickets are sold for a given route, not for a given bus. Passengers are expected
  to wait for a bus with empty seats.  However, we cannot sell more tickets for
  a given route on a given day than the number of total seats.
* Tickets for Mondays thru Thursdays are always cheaper than
  those for on Friday, Saturdays, and Sundays.
* A 10% discount should be given when 4 tickets are purchased together.
