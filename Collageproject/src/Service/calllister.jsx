const BASEURL = "https://c5a3-2409-40f0-6050-7870-2d8a-5bf0-50b4-48a4.ngrok-free.app";

export const connectIncomingCallSocket = (
  userId,
  onMessage
) => {

  if (!userId) {

    console.log("❌ userId missing");

    return null;

  }

  const wsUrl =
    `${BASEURL.replace("https", "ws")}/call/ws/call/${userId}`;

  console.log("Connecting socket:", wsUrl);

  const socket = new WebSocket(wsUrl);


  socket.onopen = () => {

    console.log("✅ socket connected");

  };


  socket.onmessage = (event) => {

    try {

      const data = JSON.parse(event.data);

      console.log("📩 socket message:", data);

      if (onMessage) {

        onMessage(data);

      }

    } catch (err) {

      console.log("❌ socket parse error", err);

    }

  };


  socket.onerror = (err) => {

    console.log("❌ socket error", err);

  };


  socket.onclose = () => {

    console.log("🔌 socket closed");

  };


  return socket;

};