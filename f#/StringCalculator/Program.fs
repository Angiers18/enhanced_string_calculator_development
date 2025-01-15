module Program

open System


[<EntryPoint>]
let main argv =

    let cleanStr (inputStr: string) : string =
        let delimiters = ['\n']
        delimiters 
        |> List.fold (fun accumulator delimit -> accumulator.Replace(delimit, ',')) inputStr

    let add (inputStr: string) : int =
        if inputStr = "" then 0
        else
            inputStr.Split(',')
            |> Array.filter (fun x -> x <> "") 
            |> Array.map int
            |> Array.sum
  
    0 // return an integer exit code


