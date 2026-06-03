import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { BrowserRouter } from "react-router-dom";
import { AppRouter } from "./router";
import ScrollToTop from "../components/ScrollToTop";
import { ThemeProvider } from "../hooks/useTheme";

const queryClient = new QueryClient();

export function App() {
  return (
    <ThemeProvider>
      <QueryClientProvider client={queryClient}>
        <BrowserRouter>
          <AppRouter />
          <ScrollToTop />
        </BrowserRouter>
      </QueryClientProvider>
    </ThemeProvider>
  );
}


