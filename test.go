package main

import (
	"fmt"
	"log"
	"math"

	pb "test/pb/go"

	"google.golang.org/protobuf/encoding/protojson"
	// Import your generated protobuf package
	// examplepb "://github.com"
)

func main() {
	// 1. Create an instance of your generated message
	msg := &pb.ExampleMessage{
		ExampleFloat: math.MaxFloat32,
	}

	// 2. Configure options (optional, e.g., pretty-printing)
	marshaller := protojson.MarshalOptions{
		Multiline: true,
		Indent:    "  ",
	}

	// 3. Encode the message to a byte slice
	bytes, err := marshaller.Marshal(msg)
	if err != nil {
		log.Fatalf("failed to encode: %v", err)
	}

	fmt.Println(string(bytes))
}
