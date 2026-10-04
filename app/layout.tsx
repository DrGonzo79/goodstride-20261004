import type {Metadata} from "next";
import "./globals.css";
export const metadata: Metadata = {title:"GoodStride — Charity bib finder",description:"Find a charity place for a major marathon and build a realistic fundraising plan."};
export default function RootLayout({children}:{children:React.ReactNode}){return <html lang="en"><body>{children}</body></html>}
