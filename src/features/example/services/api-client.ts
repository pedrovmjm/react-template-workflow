import { createApiClient } from "@/lib/api/create-api-client"

import { exampleApiConfig } from "../config"

export const exampleApi = createApiClient({
  apiVersion: exampleApiConfig.apiVersion,
  baseUrl: exampleApiConfig.baseUrl,
})
