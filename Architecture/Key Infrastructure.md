# Key Code Modules
***
## Advanced and flexible JSON parsing 
- Preferably 'node' based
- Does not require a specific structure of JSON and therefore creates a generalised object containing 'nodes'. That way a service can be parsed a collection of nodes and do its own thing with it.

## Item system
- A robust item system
- Inheritance vs Interfaced
- Struct vs Class
- JSON vs ScriptableObject
- Weapons can easily be assigned different effects or bullets
- How do the items work with the animation system
- Items should feel flexible and free to create. It should not feel like a super hard coded format.

## Data Saving and serialisation
- Full serialisation vs procedure defined save files
- Multiple save services for different data..?
- Binary data for large save information?

## State management
- How are scenes going to be managed. What objects persist
- Loading system to effectively RAM push assets whilst showing progress.

## Asset loader
- Dynamically load assets at run time
- Use key or id to request specific assets
- Allows for texture packs
- Before Gameplay, manufacture tile or item templates which can then be use to generate actual tiles
- Load dynamically from a sprite atlas