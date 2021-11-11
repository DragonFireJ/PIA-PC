function Get-Usb{
    $drives = [System.IO.DriveInfo]::GetDrives() #Obtener info de los discos
    $r = $drives | Where-Object { $_.DriveType -eq 'Removable' -and $_.IsReady } # Filtra # los removibles que esten conectados
    if ($r) { # Si encuentra uno regresa su info, si no lanza un excepcion
        return @($r)[-1]
    }
    throw "No removable drives found."
}

$usb = Get-Usb
$usb.RootDirectory.Name # Accede al directorio raíz de la usb

$ruta = (pwd).path # Genera la ruta donde estamos
$ruta = "$ruta\Usb_copy" # Creamos Usb_copy

Copy-Item -Path $usb.RootDirectory.Name -Destination $ruta -Recurse -Force -Passthru # Copia los elementos de la USB a la ruta 
