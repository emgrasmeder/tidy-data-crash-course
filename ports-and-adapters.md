# Ports and Adapters / Hexagonal / Onion Architecture 

My recommendation for how to keep your code organized is to follow the Ports and Adapters pattern. 

```
┌─────────────────────────────────────────────────────────────────┐
│port layer                                                       |
|         Code that knows about the outside world                 │
│         Causes side effects                                     │
│         Depends on state external to the app                    │
│         ┌──────────────────────────────────────────────┐        │
│         │adapter layer                                 │        │
│         │    Only exists to convert between port       |        |
|         |    and core                                  │        │
│         │        ┌────────────────────────────────┐    │        │
│         │        │ core                           │    │        │
│         │        │     Pure Functions             │    │        │
│         │        │     Domain Code                │    │        │
│         │        │     No Side Effects            │    │        │
│         │        └────────────────────────────────┘    │        │
│         └──────────────────────────────────────────────┘        │
└─────────────────────────────────────────────────────────────────┘
```

