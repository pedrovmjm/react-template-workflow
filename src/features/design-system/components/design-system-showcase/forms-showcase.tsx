import { type Dispatch, type SetStateAction } from "react"
import { BoldIcon, ItalicIcon, SparklesIcon } from "lucide-react"
import { type UseFormReturn } from "react-hook-form"

import { Calendar } from "@/components/ui/calendar"
import { Checkbox } from "@/components/ui/checkbox"
import {
  Combobox,
  ComboboxContent,
  ComboboxEmpty,
  ComboboxGroup,
  ComboboxInput,
  ComboboxItem,
  ComboboxList,
} from "@/components/ui/combobox"
import { Field, FieldDescription, FieldGroup, FieldLabel } from "@/components/ui/field"
import { FileUploadDropzone } from "@/components/ui/file-upload-dropzone"
import { Form, FormControl, FormDescription, FormField, FormItem, FormLabel, FormMessage } from "@/components/ui/form"
import { Input } from "@/components/ui/input"
import { InputGroup, InputGroupAddon, InputGroupInput } from "@/components/ui/input-group"
import { InputOTP, InputOTPGroup, InputOTPSlot } from "@/components/ui/input-otp"
import { NativeSelect, NativeSelectOption } from "@/components/ui/native-select"
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"
import { Slider } from "@/components/ui/slider"
import { Switch } from "@/components/ui/switch"
import { TabsContent } from "@/components/ui/tabs"
import { Textarea } from "@/components/ui/textarea"
import { Toggle } from "@/components/ui/toggle"
import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group"

import { type DemoForm } from "./showcase-data"
import { ShowcaseCard } from "./showcase-card"

type FormsShowcaseProps = {
  form: UseFormReturn<DemoForm>
  setUploadedFiles: Dispatch<SetStateAction<File[]>>
  uploadedFiles: File[]
}

export function FormsShowcase({ form, setUploadedFiles, uploadedFiles }: FormsShowcaseProps) {
  return (
    <TabsContent value="forms" className="grid gap-4 lg:grid-cols-2">
      <ShowcaseCard title="Campos" description="field, input, input-group, textarea, select, native-select e combobox.">
        <FieldGroup>
          <Field>
            <FieldLabel htmlFor="search">Busca</FieldLabel>
            <Input id="search" placeholder="Buscar componente" />
            <FieldDescription>Input shadcn estilizado pelos tokens globais.</FieldDescription>
          </Field>
          <Field>
            <FieldLabel htmlFor="amount">Valor</FieldLabel>
            <InputGroup>
              <InputGroupAddon>R$</InputGroupAddon>
              <InputGroupInput id="amount" placeholder="0,00" />
            </InputGroup>
          </Field>
          <Field>
            <FieldLabel>Categoria</FieldLabel>
            <Select defaultValue="contas">
              <SelectTrigger className="w-full" aria-label="Categoria">
                <SelectValue placeholder="Selecione" />
              </SelectTrigger>
              <SelectContent>
                <SelectGroup>
                  <SelectItem value="contas">Contas</SelectItem>
                  <SelectItem value="cartoes">Cartoes</SelectItem>
                  <SelectItem value="seguros">Seguros</SelectItem>
                </SelectGroup>
              </SelectContent>
            </Select>
          </Field>
          <Field>
            <FieldLabel htmlFor="native-payment-method">Native select</FieldLabel>
            <NativeSelect id="native-payment-method" defaultValue="pix" className="w-full">
              <NativeSelectOption value="pix">Pix</NativeSelectOption>
              <NativeSelectOption value="ted">TED</NativeSelectOption>
            </NativeSelect>
          </Field>
          <Field>
            <FieldLabel>Combobox</FieldLabel>
            <Combobox>
              <ComboboxInput aria-label="Servico" placeholder="Selecionar servico" />
              <ComboboxContent>
                <ComboboxList>
                  <ComboboxEmpty>Nenhum servico</ComboboxEmpty>
                  <ComboboxGroup>
                    <ComboboxItem value="Conta digital">Conta digital</ComboboxItem>
                    <ComboboxItem value="Cartoes">Cartoes</ComboboxItem>
                  </ComboboxGroup>
                </ComboboxList>
              </ComboboxContent>
            </Combobox>
          </Field>
          <Field>
            <FieldLabel htmlFor="notes">Observacoes</FieldLabel>
            <Textarea id="notes" placeholder="Descreva o caso de uso" />
          </Field>
        </FieldGroup>
      </ShowcaseCard>

      <ShowcaseCard title="Controles" description="calendar, checkbox, radio-group, switch, slider, toggle, toggle-group, input-otp e form.">
        <div className="grid gap-4 md:grid-cols-[260px_minmax(0,1fr)]">
          <Calendar mode="single" selected={new Date(2026, 4, 13)} />
          <FieldGroup>
            <Field orientation="horizontal">
              <Checkbox id="notifications" defaultChecked />
              <FieldLabel htmlFor="notifications">Receber novidades</FieldLabel>
            </Field>
            <Field orientation="horizontal">
              <Switch id="compact-mode" defaultChecked />
              <FieldLabel htmlFor="compact-mode">Modo compacto</FieldLabel>
            </Field>
            <RadioGroup defaultValue="app" className="flex gap-3">
              <Field orientation="horizontal">
                <RadioGroupItem id="channel-app" value="app" />
                <FieldLabel htmlFor="channel-app">App</FieldLabel>
              </Field>
              <Field orientation="horizontal">
                <RadioGroupItem id="channel-web" value="web" />
                <FieldLabel htmlFor="channel-web">Web</FieldLabel>
              </Field>
            </RadioGroup>
            <Slider aria-label="Valor de exemplo" defaultValue={[60]} max={100} step={10} />
            <ToggleGroup type="multiple" variant="outline">
              <ToggleGroupItem value="bold" aria-label="Negrito">
                <BoldIcon />
              </ToggleGroupItem>
              <ToggleGroupItem value="italic" aria-label="Italico">
                <ItalicIcon />
              </ToggleGroupItem>
            </ToggleGroup>
            <Toggle variant="outline" aria-label="Favorito">
              <SparklesIcon />
            </Toggle>
            <InputOTP aria-label="Codigo de exemplo" maxLength={4} value="2026" readOnly>
              <InputOTPGroup>
                <InputOTPSlot index={0} />
                <InputOTPSlot index={1} />
                <InputOTPSlot index={2} />
                <InputOTPSlot index={3} />
              </InputOTPGroup>
            </InputOTP>
          </FieldGroup>
        </div>
        <Form {...form}>
          <FormField
            control={form.control}
            name="cliente"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Form shadcn</FormLabel>
                <FormControl>
                  <Input {...field} />
                </FormControl>
                <FormDescription>Contrato react-hook-form integrado.</FormDescription>
                <FormMessage />
              </FormItem>
            )}
          />
        </Form>
      </ShowcaseCard>

      <ShowcaseCard
        title="Upload de arquivos"
        description="Componente pronto com input real, clique para selecionar e drag and drop."
        className="lg:col-span-2"
      >
        <FileUploadDropzone
          accept=".csv,.pdf,.png,.jpg,.jpeg"
          files={uploadedFiles}
          label="Enviar documentos"
          description="Solte arquivos aqui ou selecione CSV, PDF e imagens para anexar ao fluxo."
          onFilesChange={setUploadedFiles}
        />
      </ShowcaseCard>
    </TabsContent>
  )
}
