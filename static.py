import asyncio
import subprocess

#our function
async def set_static_ip(device_name, ip_address, subnet_mask, gateway):
    command = f"netsh interface ip set address name='{device_name}' static {ip_address} {subnet_mask} {gateway} 1"
    process = await asyncio.create_subprocess_shell(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    _, stderr = await process.communicate()

    if process.returncode != 0:
        error_message = stderr.decode(errors='replace').strip()
        raise RuntimeError(f"Failed to set static IP: {error_message}")


#Example how to use it
async def main():
     tasks = [
         set_static_ip('Ethernet', '192.168.1.100', '255.255.255.0', '192.168.1.1'),
         set_static_ip('Wi-Fi', '192.168.1.101', '255.255.255.0', '192.168.1.1')
     ]
     results = await asyncio.gather(*tasks, return_exceptions=True)

asyncio.run(main())
