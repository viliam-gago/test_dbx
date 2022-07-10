# Databricks notebook source
storage_account_name = "formula1dlvg"
client_id = "7ec212bb-fb63-44a1-9bec-05646ba62964"
tenant_id = "e25a37ae-1f15-4f21-a941-54784a40e76b"
client_secret = "taR8Q~_yrmtHMhfCIy7AFkJeGsfklX.UA54mMc32"

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
       "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
       "fs.azure.account.oauth2.client.id": f"{client_id}",
       "fs.azure.account.oauth2.client.secret": f"{client_secret}",
       "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id}/oauth2/token",
#        "fs.azure.createRemoteFileSystemDuringInitialization": "true"
}

# COMMAND ----------

def mount_adls(conatiner_name):
    dbutils.fs.mount(
        source = f"abfss://{conatiner_name}@{storage_account_name}.dfs.core.windows.net/",
        mount_point = f"/mnt/{storage_account_name}/{conatiner_name}",
        extra_configs = configs
    )

# COMMAND ----------

for mount in dbutils.fs.ls("/mnt/formula1dlvg"):
    print(mount.name)

# COMMAND ----------

for mt_name in dbutils.fs.mounts():
    print(mt_name.mountPoint)

# COMMAND ----------

mount_adls('processed')

# COMMAND ----------

dbutils.fs.unmount("/mnt/formula1dlvg/processed")

# COMMAND ----------

