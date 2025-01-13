module Program

open System


[<EntryPoint>]
let main argv =
    let add (inputStr: string) : int =
        if inputStr = "" then 0
        else
            let splitStr = inputStr.Split(',') |> Array.map int
            if splitStr |> Array.exists (fun x -> x > 2) then
                failwith "No se puede sumar números mayores a 2"
            else
                splitStr |> Array.sum

    0 // Código de salida






