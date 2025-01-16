module Program

open System


[<EntryPoint>]
let main argv =
    let cleanStr (inputStr: string) : string =
        let delimiters = ['\n' ; '+'; '*'; '/'; ';'; ':'; '['; ']'; '%'; '^'; '&'; '|'; '!'; '?'; '~'; '('; ')'; '{'; '}'; '<'; '>' ; '.']
        delimiters 
        |> List.fold (fun accumulator delimit -> accumulator.Replace(delimit, ',')) inputStr

    let add (inputStr: string) : int =
     try
        if inputStr = "" then 0
        else
            let numbers =
                inputStr.Split(',')
                |> Array.filter (fun x -> x <> "") // Filtrar elementos vacíos
                |> Array.map int // Convertir a enteros

            let negatives = numbers |> Array.filter (fun x -> x < 0)

            if negatives.Length > 0 then
                let negativeString = negatives |> Array.map string |> String.concat ", "
                failwith ("Negatives not allowed: " + negativeString)
            else
                numbers |> Array.sum
     with
     | ex -> 
        printfn "Error: %s" ex.Message
        -1 // Returns -1 in case of error 

    printfn "Enter the numbers to add: example 1,2,3,4,5"
    let inputStr = Console.ReadLine()
    printfn "The result of the sum is %d" (add (cleanStr inputStr))  
    

    0 // everything well

    
    
    
