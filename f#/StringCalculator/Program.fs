module Program

open System


[<EntryPoint>]
let main argv =
    let cleanStr (input: string) : string =
        let delimiters = ['\n' ; '+'; '*'; '/'; ';'; ':'; '['; ']'; '%'; '^'; '&'; '|'; '!'; '?'; '~'; '('; ')'; '{'; '}'; '<'; '>' ; '.']
        delimiters 
        |> List.fold (fun accumulator delimit -> accumulator.Replace(delimit, ',')) input

    let add (inputStr: string) : int =
     try
        if inputStr = "" then 0
        else
            let numbers =
                inputStr.Split(',')
                |> Array.filter (fun x -> x <> "")
                |> Array.map int

            let negatives = numbers |> Array.filter (fun x -> x < 0)

            if negatives.Length > 0 then
                let negativeString = negatives |> Array.map string |> String.concat ", "
                failwith ("negatives not allowed: " + negativeString)
            else

                if numbers |> Array.exists (fun x -> x > 1000) then
                    let numbersLessThan1000 = numbers |> Array.filter (fun x -> x <= 1000)
                    numbersLessThan1000 |> Array.sum
                else 
                numbers |> Array.sum
     with
     | ex -> 
        printfn "Error: %s" ex.Message
        -1 // Returns -1 in case of error 

   
    0 // everything well