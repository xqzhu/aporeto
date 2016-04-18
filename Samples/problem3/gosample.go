package main

import "fmt"
import "os"
import "strings"
import "net/http"
import "io/ioutil"
import "log"
import "regexp"
import "strconv"
func main() {
    if len(os.Args) > 1 {
        argList := os.Args[1:]
        if len(argList) == 1 {
            
            if argList[0] == "-h" {
                fmt.Println("Usage:")
                fmt.Println("gosample [-help|-h]")
                fmt.Println("gosample -urls=<url1>[,<url2>[,<url3>[,<url4>]]]")
                os.Exit(0)
            }
            if argList[0] == "-help" {
                fmt.Println("Usage:")
                fmt.Println("gosample [-help|-h]")
                fmt.Println("gosample -urls=<url1>[,<url2>[,<url3>[,<url4>]]]")
                os.Exit(0)
            }
            
            startsWith := strings.HasPrefix(argList[0], "-urls=")
            if startsWith == true {
                uList := strings.TrimLeft(argList[0], "-urls=")
                urlList := strings.Split(uList, ",")
                for index, url := range urlList {
                    res, err := http.Get(url)
                    checkError(err)
                    data, err := ioutil.ReadAll(res.Body)
                    checkError(err)
                    text := string(data)
                    file_out(count_words(get_words_from(text)), index + 1)
                }
                os.Exit(0)
            }
        }
        fmt.Println("Usage:")
        fmt.Println("gosample [-help|-h]")
        fmt.Println("gosample -urls=<url1>[,<url2>[,<url3>[,<url4>]]]")
    }
}

func checkError(err error) {
    if err != nil {
        log.Fatalf("Error : %v", err)
        os.Exit(1)
    }
}

func get_words_from(text string) []string{
    words := regexp.MustCompile("[a-zA-Z0-9]+")
    return words.FindAllString(text, -1)
}

func count_words (words []string) map[string]int{
    word_counts := make(map[string]int)
    for _, word := range words{
        word_counts[word]++
    }
    return word_counts;
}

func file_out (word_counts map[string]int, appendix int){
    outfile, err := os.Create("url" + strconv.Itoa(appendix) + ".txt")
    checkError(err)
    for word, word_count := range word_counts{
        //fmt.Printf("%v %v\n", word, word_count)
        line := word + " " + strconv.Itoa(word_count) + "\n"
        outfile.WriteString(line)
    }
}