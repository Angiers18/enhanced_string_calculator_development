module Program

open System


[<EntryPoint>]
let main argv =
    let add (inputStr: string) : int =
        if inputStr = "" then 0
        else
            let splitStr = inputStr.Split(',') |> Array.map int
            splitStr |> Array.sum

    0 // return an integer exit code






