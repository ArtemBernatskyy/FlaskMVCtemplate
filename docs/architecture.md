### How to add new app
1. Create module in `transfer_sys.app` with the name of your app (for example `transfer_sys.app.new_app`)  
2. Add `models.py` to `transfer_sys.app.new_app` where describe your models  
3. Add `urls.py` to `transfer_sys.app.new_app` where create your blueprints   
4. Register blueprints in `transfer_sys.urls.py`  