## BoringShepherd

The BoringShepherd class is a base class for 
all Shepherds, who are the keepers (and constructors)
of the flock.

The BoringShepherd class leaves the details of 
creating the sheep to the user, but it defines
a few useful methods.

The BoringSheep constructor calls a method to set up 
the flock. The method to set up the flock loops over 
each key. For each key, it:

- validates the key
- creates a Sheep from the key

There are also two methods to perform actions with the flock:
one for serial and one for parallel.

