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
  const [isDragging, setIsDragging] = React.useState(false)
  const [internalFiles, setInternalFiles] = React.useState<File[]>([])
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

    updateFiles(Array.from(fileList))
  }

  function removeFile(fileName: string) {
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

      {selectedFiles.length > 0 ? (
        <div className="flex flex-col gap-2" aria-live="polite">
          {selectedFiles.map((file) => (
            <div
              key={`${file.name}-${file.size}`}
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
