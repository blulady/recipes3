- add some sort of rating method so people could vote on recipe & organize the list view to show the most popular 
- add admin/permissions to edit/delete diets
- edit/delete on recipes only for those who added those recipes
- a favorites that a user can keep their favorites as they are even if the owner deletes/updates them
<<<<<<< HEAD
- form help texts are not showing up but the ones from models are showing up... why?
=======
- a test
- 
>>>>>>> 7588242894ee1d4153f4da89f54887515de76f4d
[link](https://fly.io/docs/getting-started/troubleshooting/#health-checks-failing)

Greeings Customer,
I am sorry to hear that a small change is now affecting your ability to deploy. I am sure that you already saw the Health Checks failing section of the trouble shooting docs but if not, check this [link](https://fly.io/docs/getting-started/troubleshooting/#health-checks-failing) out. I would appreciate some information about the app, as what kind of app are you trying to deploy, any other erros you can see and recent change that you made. On my end I will be checking the VM's to make sure they are shutting down and rebuilding appropriately 

---

#### Support Email Troubleshooting steps
- run fly status --all #this should show failing VMs
- run fly vm status id# on the failing VMs
- enable debug loggin
  - LOG_LEVEL=debug fly deploy --verbose
  - LOG_LEVEL=debug fly deploy --remote-only --verbose
