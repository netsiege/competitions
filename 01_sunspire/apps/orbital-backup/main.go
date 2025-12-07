package main

import (
	"archive/zip"
	"io"
	"log"
	"os"
	"path/filepath"
	"time"

	"github.com/kardianos/service"
)

const (
	sourceDir   = `C:\Shares\public`
	backupPath  = `C:\Program Files\SunSpire Backup\backup.zip`
	intervalMin = 300
)

type program struct{}

func (p *program) Start(s service.Service) error {
	go p.run()
	return nil
}

func (p *program) run() {
	// Run backup immediately on start
	doBackup()

	// Then run every 300 minutes
	ticker := time.NewTicker(time.Duration(intervalMin) * time.Minute)
	for range ticker.C {
		doBackup()
	}
}

func (p *program) Stop(s service.Service) error {
	return nil
}

func doBackup() {
	log.Println("Starting backup...")

	// Ensure backup directory exists
	backupDir := filepath.Dir(backupPath)
	if err := os.MkdirAll(backupDir, 0755); err != nil {
		log.Printf("Failed to create backup directory: %v", err)
		return
	}

	// Create zip file
	zipFile, err := os.Create(backupPath)
	if err != nil {
		log.Printf("Failed to create backup file: %v", err)
		return
	}
	defer zipFile.Close()

	zipWriter := zip.NewWriter(zipFile)
	defer zipWriter.Close()

	// Walk source directory and add files to zip
	err = filepath.Walk(sourceDir, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}

		// Skip directories
		if info.IsDir() {
			return nil
		}

		// Get relative path for zip entry
		relPath, err := filepath.Rel(sourceDir, path)
		if err != nil {
			return err
		}

		// Create zip entry
		writer, err := zipWriter.Create(relPath)
		if err != nil {
			return err
		}

		// Open source file
		file, err := os.Open(path)
		if err != nil {
			return err
		}
		defer file.Close()

		// Copy contents
		_, err = io.Copy(writer, file)
		return err
	})

	if err != nil {
		log.Printf("Backup failed: %v", err)
		return
	}

	log.Println("Backup completed successfully")
}

func main() {
	svcConfig := &service.Config{
		Name:        "SunSpireBackup",
		DisplayName: "SunSpire Backup Agent",
		Description: "Backs up SMB share contents periodically",
	}

	prg := &program{}
	s, err := service.New(prg, svcConfig)
	if err != nil {
		log.Fatal(err)
	}

	// Handle service control commands
	if len(os.Args) > 1 {
		switch os.Args[1] {
		case "install":
			err = s.Install()
			if err != nil {
				log.Fatal("Failed to install service: ", err)
			}
			log.Println("Service installed")
			return
		case "uninstall":
			err = s.Uninstall()
			if err != nil {
				log.Fatal("Failed to uninstall service: ", err)
			}
			log.Println("Service uninstalled")
			return
		case "start":
			err = s.Start()
			if err != nil {
				log.Fatal("Failed to start service: ", err)
			}
			log.Println("Service started")
			return
		case "stop":
			err = s.Stop()
			if err != nil {
				log.Fatal("Failed to stop service: ", err)
			}
			log.Println("Service stopped")
			return
		}
	}

	// Run the service
	err = s.Run()
	if err != nil {
		log.Fatal(err)
	}
}
