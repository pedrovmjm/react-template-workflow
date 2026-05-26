import * as React from "react"
import { FileIcon, UploadCloudIcon, XIcon } from "lucide-react"

import { Button } from "@/components/ui/button"
import { cn } from "@/lib/utils"

type FileUploadDropzoneProps = Omit<
  React.ComponentProps<"input">,
  "className" | "files" | "onChange" | "type" | "value"
> & {
  className?: string
  description?: string
  files?: File[]
  label?: string
  maxFiles?: number
  onFilesChange?: (files: File[]) => void
}

function fileKey(file: File) {
  return `${file.name}-${file.size}`
}

function partitionIncomingFiles(incoming: File[], existing: File[]) {
  const existingKeys = new Set(existing.map(fileKey))
  const seenIncoming = new Set<string>()
  const accepted: File[] = []
  const duplicateNames: string[] = []

  for (const file of incoming) {
    const key = fileKey(file)

    if (existingKeys.has(key) || seenIncoming.has(key)) {
      if (!duplicateNames.includes(file.name)) {
        duplicateNames.push(file.name)
      }
      continue
    }

    seenIncoming.add(key)
    accepted.push(file)
  }

  return { accepted, duplicateNames }
}

function formatFileSize(size: number) {
  if (size < 1024) {
    return `${size} B`
  }

  if (size < 1024 * 1024) {
    return `${Math.round(size / 1024)} KB`
  }

  return `${(size / 1024 / 1024).toFixed(1)} MB`
}

function FileUploadDropzone({
  accept,
  className,
  description = "Arraste arquivos para ca ou selecione no computador.",
  disabled,
  files,
  id,
  label = "Upload de arquivos",
  maxFiles = 4,
  multiple = true,
  onFilesChange,
  ...props
}: FileUploadDropzoneProps) {
  const generatedId = React.useId()
  const inputId = id ?? generatedId
  const inputRef = React.useRef<HTMLInputElement>(null)
  const errorId = `${inputId}-error`
  const [isDragging, setIsDragging] = React.useState(false)
  const [internalFiles, setInternalFiles] = React.useState<File[]>([])
  const [validationError, setValidationError] = React.useState<string | null>(null)
  const selectedFiles = files ?? internalFiles

  const updateFiles = React.useCallback(
    (nextFiles: File[]) => {
      const limitedFiles = nextFiles.slice(0, multiple ? maxFiles : 1)

      if (!files) {
        setInternalFiles(limitedFiles)
      }

      onFilesChange?.(limitedFiles)
    },
    [files, maxFiles, multiple, onFilesChange],
  )

  function handleFiles(fileList: FileList | null) {
    if (!fileList) {
      return
    }

    const incoming = Array.from(fileList)
    const messages: string[] = []

    if (!multiple) {
      const { accepted, duplicateNames } = partitionIncomingFiles(
        incoming.slice(0, 1),
        selectedFiles,
      )

      if (duplicateNames.length > 0) {
        messages.push(`O arquivo "${duplicateNames[0]}" já foi adicionado.`)
      }

      if (accepted.length > 0) {
        updateFiles(accepted)
      }

      setValidationError(messages.length > 0 ? messages.join(" ") : null)

      if (inputRef.current) {
        inputRef.current.value = ""
      }
      return
    }

    const { accepted, duplicateNames } = partitionIncomingFiles(incoming, selectedFiles)

    if (duplicateNames.length > 0) {
      messages.push(
        duplicateNames.length === 1
          ? `O arquivo "${duplicateNames[0]}" já foi adicionado.`
          : `Estes arquivos já foram adicionados: ${duplicateNames.join(", ")}.`,
      )
    }

    const availableSlots = Math.max(maxFiles - selectedFiles.length, 0)
    const filesToAdd = accepted.slice(0, availableSlots)

    if (accepted.length > availableSlots) {
      messages.push(`Limite de ${maxFiles} arquivos.`)
    }

    if (filesToAdd.length > 0) {
      updateFiles([...selectedFiles, ...filesToAdd])
    }

    setValidationError(messages.length > 0 ? messages.join(" ") : null)

    if (inputRef.current) {
      inputRef.current.value = ""
    }
  }

  function removeFile(fileName: string) {
    setValidationError(null)
    updateFiles(selectedFiles.filter((file) => file.name !== fileName))
  }

  return (
    <div className={cn("flex flex-col gap-3", className)}>
      <input
        ref={inputRef}
        id={inputId}
        type="file"
        accept={accept}
        disabled={disabled}
        multiple={multiple}
        className="sr-only"
        onChange={(event) => handleFiles(event.target.files)}
        {...props}
      />
      <div
        aria-disabled={disabled}
        aria-describedby={validationError ? errorId : undefined}
        aria-invalid={validationError ? true : undefined}
        onDragEnter={(event) => {
          event.preventDefault()
          if (!disabled) {
            setIsDragging(true)
          }
        }}
        onDragLeave={(event) => {
          event.preventDefault()
          setIsDragging(false)
        }}
        onDragOver={(event) => {
          event.preventDefault()
        }}
        onDrop={(event) => {
          event.preventDefault()
          setIsDragging(false)

          if (!disabled) {
            handleFiles(event.dataTransfer.files)
          }
        }}
        className={cn(
          "flex min-h-48 flex-col items-center justify-center gap-3 rounded-lg border border-dashed bg-muted p-6 text-center transition-colors",
          isDragging && "border-primary bg-primary/5",
          validationError && "border-destructive ring-destructive/20",
          disabled && "pointer-events-none opacity-50",
        )}
      >
        <span className="flex size-11 items-center justify-center rounded-full bg-background text-primary">
          <UploadCloudIcon aria-hidden="true" />
        </span>
        <div className="flex max-w-md flex-col gap-1">
          <label htmlFor={inputId} className="text-sm font-semibold">
            {label}
          </label>
          <p className="text-sm text-muted-foreground">{description}</p>
        </div>
        <Button
          type="button"
          variant="secondary"
          disabled={disabled}
          onClick={() => inputRef.current?.click()}
        >
          <UploadCloudIcon data-icon="inline-start" />
          Selecionar arquivos
        </Button>
      </div>

      {validationError ? (
        <p id={errorId} role="alert" className="text-sm text-destructive">
          {validationError}
        </p>
      ) : null}

      {selectedFiles.length > 0 ? (
        <div className="flex flex-col gap-2" aria-live="polite">
          {selectedFiles.map((file) => (
            <div
              key={fileKey(file)}
              className="flex items-center gap-3 rounded-md border bg-background px-3 py-2"
            >
              <FileIcon aria-hidden="true" />
              <div className="min-w-0 flex-1">
                <p className="truncate text-sm font-medium">{file.name}</p>
                <p className="text-xs text-muted-foreground">{formatFileSize(file.size)}</p>
              </div>
              <Button
                type="button"
                size="icon-sm"
                variant="ghost"
                aria-label={`Remover ${file.name}`}
                onClick={() => removeFile(file.name)}
              >
                <XIcon />
              </Button>
            </div>
          ))}
        </div>
      ) : null}
    </div>
  )
}

export { FileUploadDropzone }
