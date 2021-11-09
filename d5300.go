package main

import (
	"os"
	"log"
	"strconv"
	"github.com/atotto/ptpip"
	"github.com/atotto/ptpip/ptp"
	"github.com/spf13/cobra"
)

func main() {
	var err error
	var name string
	var guid string
	var config *ptpip.Config
	var addr string
        var port int16
        var verbose bool
	var client *ptpip.Client

	var rootCmd = &cobra.Command{
                Use:   "",
                Short: "use Picture Transfer Protocol over IP on target",
                // Args:  ,
                Run: func(cmd *cobra.Command, args []string) {
		},
		PersistentPreRun: func(cmd *cobra.Command, args []string) {
			log.Println("Network configuration...")
			config, err = ptpip.NewConfig(guid, name)
			if err != nil {
				log.Println("Error while creating config: %s", err)
				return
			}
			var addrStr = addr + ":" + strconv.FormatInt(int64(port), 10)
			log.Println("Connecting to %s...", addrStr)

			client, err = ptpip.DialConfig(addrStr, config)
			if err != nil {
				log.Println("Error while connecting: %s", err)
				return
			}
			log.Println("Connected !")
		},
	}
	
	rootCmd.PersistentFlags().StringVarP(&name, "name", "n", "Default too long nameeeeeee", "Config name")
	rootCmd.PersistentFlags().StringVarP(&guid, "guid", "g", "bca6141c-eca3-400b-82ad-08c84c5770b4", "guid")
	rootCmd.PersistentFlags().StringVarP(&addr, "ip", "t", "192.168.1.1", "Target camera IP")
        rootCmd.PersistentFlags().Int16VarP(&port, "port", "p", 15740, "Target camera PTP/IP port")
        rootCmd.PersistentFlags().BoolVarP(&verbose, "verbose", "v", false, "Print verbose output")


	var still = &cobra.Command{
		Use: "still",
		Short: "capture image",
		Run: func(cmd *cobra.Command, args []string) {
			sessionId := uint32(1)
			log.Println("Open session")
			
			err = client.OperationSimple(ptp.OC_OpenSession, 1, []uint32{ sessionId })
			if err != nil {
				log.Println("Error while opening session: %s", err)
				return
			}
			log.Println("Initiate capture")
			err = client.OperationSimple(ptp.OC_InitiateCapture, 2, []uint32{ 0, 0 })
			if err != nil {
				log.Println("Error while capture: %s", err)
				return
			}
			log.Println("Close session")
			err = client.OperationSimple(ptp.OC_CloseSession, 3, []uint32{})
			if err != nil {
				log.Println("Error while closing session: %s", err)
				return
			}
		},
	}

        rootCmd.AddCommand(still)

        if err := rootCmd.Execute(); err != nil {
                log.Println(err)
                os.Exit(1)
        }
}

