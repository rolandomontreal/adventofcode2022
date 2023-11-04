package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type directory struct {
	name string
	parent *directory
	subDirectories []directory
	files []file
	size int
}

type file struct {
	name string
	size int
}

func main() {
	data, err := os.ReadFile("./testdata.txt")

	if err != nil {
		fmt.Println("Error reading file: ", err)
	}

	var cwd *directory
	var rootDir *directory

	terminalOutputRaw := string(data)
	terminalRows := strings.Split(terminalOutputRaw, "\n")[:23]

	for _, terminalRow := range terminalRows {
		fmt.Println(terminalRow)
		parts := strings.Split(terminalRow, " ")

		// Command
		if parts[0] == "$" {
			fmt.Println("Is a command...")
			command := parts[1]
			if command == "cd" {
				fmt.Println("Change directory...")
				directoryName := parts[2]
				fmt.Println("Directory name: ", directoryName)
				
				if directoryName == ".." {
					cwd = cwd.parent
				} else if (cwd == nil) {
					d := directory{
						name: directoryName,
						subDirectories: []directory{},
						files: []file{},
					}
					cwd = &d
					rootDir = &d
					fmt.Printf("%p\n", &d)
					fmt.Printf("%p\n", &cwd)
					fmt.Println("Setting root node...", cwd)
				} else {
					nextDirFound := false
					for i := 0; i < len(cwd.subDirectories) && !nextDirFound; i++ {
						dir := cwd.subDirectories[i]
						fmt.Println("Dir checking: ", dir)
						if dir.name == directoryName {
							nextDirFound = true
							fmt.Println("FOUND MATCH ")
							cwd = &cwd.subDirectories[i]
						}
					}
				}
			} else if command == "ls" {
				fmt.Println("List items in directory...")
			}
		} else { // File or directory 
			if parts[0] == "dir" {
				// fmt.Println("TODO -Listing a directory")
				dirname := parts[1]
				foundDir := false
				for i := 0; i < len(cwd.subDirectories) && !foundDir; i++ {
					if cwd.name == dirname {
						foundDir = true
					}
				}
				if (foundDir) {
					fmt.Println("Directory HAS ALREADY been added...")
				} else {
					fmt.Println("NEW directory")
					d := directory {
						name: dirname,
						parent: cwd,
						subDirectories: []directory{},
						files: []file{},
					}
					cwd.subDirectories = append(cwd.subDirectories, d)
				}
			} else {	// Handle file
				size, err := strconv.Atoi(parts[0])
				if err != nil {
					fmt.Println("Error parsing file size: ", err)
					os.Exit(1)
				}
				fmt.Println("File size: ", size)
				f := file{
					name: parts[1],
					size: size,
				}
				cwd.files = append(cwd.files, f)
				cwd.size += size
				fmt.Println(cwd)
			}
		}
		fmt.Println()
	}
	
	fmt.Println("cwd: ", cwd)
	fmt.Println("root: ", rootDir)
}