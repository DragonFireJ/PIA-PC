function Get-Usb{
    $drives = [System.IO.DriveInfo]::GetDrives()
    $r = $drives | Where-Object { $_.DriveType -eq 'Removable' -and $_.IsReady }
    if ($r) {
        return @($r)[-1]
    }
    throw "No removable drives found."
}

$usb = Get-Usb
$usb.RootDirectory.Name

$ruta = Get-Location

New-Item -Path -Path $ruta\Usb_Copy\ -ItemType directory -Force 
Copy-Item -Path $usb.RootDirectory.Name -Destination $ruta\Usb_Copy\ -Recurse -Force -Passthru
