# BoringSheep

The BoringSheep class is left intentionally non-functional,
to keep from imposing any restrictions. All it does is 
implement a virtual constructor, and a `perform_action()`
method (along with one dummy action).

The `perform_action()` method is the decision-making center
of the Sheep's brain. It uses the dispatcher method to look
for a method with a name matching the requested action.

Sheep classes are typically filled with long litanies of
short functions that call various API endpoints.

