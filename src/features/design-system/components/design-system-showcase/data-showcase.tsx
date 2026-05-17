import { type Dispatch, type SetStateAction } from "react"
import { Bar, BarChart, CartesianGrid, XAxis } from "recharts"
import { CreditCardIcon, EyeIcon, SearchIcon, Trash2Icon } from "lucide-react"

import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "@/components/ui/alert-dialog"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { Card, CardContent } from "@/components/ui/card"
import { Carousel, CarouselContent, CarouselItem, CarouselNext, CarouselPrevious } from "@/components/ui/carousel"
import { ChartContainer, ChartTooltip, ChartTooltipContent } from "@/components/ui/chart"
import { Checkbox } from "@/components/ui/checkbox"
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle, DialogTrigger } from "@/components/ui/dialog"
import { Empty, EmptyDescription, EmptyHeader, EmptyMedia, EmptyTitle } from "@/components/ui/empty"
import { InputGroup, InputGroupAddon, InputGroupInput } from "@/components/ui/input-group"
import { Item, ItemContent, ItemDescription, ItemGroup, ItemMedia, ItemTitle } from "@/components/ui/item"
import { NativeSelect, NativeSelectOption } from "@/components/ui/native-select"
import { Progress } from "@/components/ui/progress"
import { ResizableHandle, ResizablePanel, ResizablePanelGroup } from "@/components/ui/resizable"
import { ScrollArea } from "@/components/ui/scroll-area"
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table"
import { TabsContent } from "@/components/ui/tabs"
import { Tooltip, TooltipContent, TooltipTrigger } from "@/components/ui/tooltip"

import { chartConfig, chartData, type OperationalRow, services } from "./showcase-data"
import { ShowcaseCard } from "./showcase-card"

type DataShowcaseProps = {
  categoryFilter: string
  filteredRows: OperationalRow[]
  setCategoryFilter: Dispatch<SetStateAction<string>>
  setRemovedRowIds: Dispatch<SetStateAction<string[]>>
  setStatusFilter: Dispatch<SetStateAction<string>>
  setTableQuery: Dispatch<SetStateAction<string>>
  statusFilter: string
  tableQuery: string
  tableRows: OperationalRow[]
}

export function DataShowcase({
  categoryFilter,
  filteredRows,
  setCategoryFilter,
  setRemovedRowIds,
  setStatusFilter,
  setTableQuery,
  statusFilter,
  tableQuery,
  tableRows,
}: DataShowcaseProps) {
  return (
    <TabsContent value="data" className="grid gap-4 lg:grid-cols-2">
      <ShowcaseCard
        title="Tabela operacional"
        description="table, input-group, select, native-select, checkbox, dropdown-menu, badge, busca, filtros e estado vazio."
        className="lg:col-span-2"
      >
        <div className="grid gap-3 lg:grid-cols-[minmax(260px,1fr)_180px_180px_auto]">
          <InputGroup>
            <InputGroupAddon>
              <SearchIcon />
            </InputGroupAddon>
            <InputGroupInput
              value={tableQuery}
              onChange={(event) => setTableQuery(event.target.value)}
              placeholder="Buscar por ID, servico ou squad"
              aria-label="Buscar tabela operacional"
            />
          </InputGroup>

          <Select value={statusFilter} onValueChange={setStatusFilter}>
            <SelectTrigger className="w-full" aria-label="Filtrar status">
              <SelectValue placeholder="Status" />
            </SelectTrigger>
            <SelectContent>
              <SelectGroup>
                <SelectItem value="all">Todos status</SelectItem>
                <SelectItem value="ativo">Ativo</SelectItem>
                <SelectItem value="revisao">Revisao</SelectItem>
                <SelectItem value="pausado">Pausado</SelectItem>
              </SelectGroup>
            </SelectContent>
          </Select>

          <NativeSelect
            value={categoryFilter}
            onChange={(event) => setCategoryFilter(event.target.value)}
            className="w-full"
            aria-label="Filtrar categoria"
          >
            <NativeSelectOption value="all">Todas categorias</NativeSelectOption>
            <NativeSelectOption value="Contas">Contas</NativeSelectOption>
            <NativeSelectOption value="Pagamentos">Pagamentos</NativeSelectOption>
            <NativeSelectOption value="Credito">Credito</NativeSelectOption>
            <NativeSelectOption value="Wealth">Wealth</NativeSelectOption>
            <NativeSelectOption value="Protecao">Protecao</NativeSelectOption>
          </NativeSelect>

          <Button
            variant="outline"
            onClick={() => {
              setTableQuery("")
              setStatusFilter("all")
              setCategoryFilter("all")
            }}
          >
            Limpar
          </Button>
        </div>

        <div className="flex flex-wrap items-center justify-between gap-3">
          <p className="text-sm text-muted-foreground">
            {filteredRows.length} de {tableRows.length} resultados
          </p>
          <div className="flex flex-wrap gap-2">
            <Badge variant="secondary">busca</Badge>
            <Badge variant="secondary">filtros</Badge>
            <Badge variant="secondary">acoes por linha</Badge>
          </div>
        </div>

        <div className="overflow-hidden rounded-lg border">
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead className="w-10">
                  <Checkbox aria-label="Selecionar todos" />
                </TableHead>
                <TableHead>ID</TableHead>
                <TableHead>Servico</TableHead>
                <TableHead>Categoria</TableHead>
                <TableHead>Status</TableHead>
                <TableHead>Squad</TableHead>
                <TableHead className="text-right">Conversao</TableHead>
                <TableHead className="w-16 text-right">Acoes</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {filteredRows.length > 0 ? (
                filteredRows.map((row) => (
                  <TableRow key={row.id}>
                    <TableCell>
                      <Checkbox aria-label={`Selecionar ${row.service}`} />
                    </TableCell>
                    <TableCell className="font-medium">{row.id}</TableCell>
                    <TableCell>{row.service}</TableCell>
                    <TableCell>{row.category}</TableCell>
                    <TableCell>
                      <Badge variant={row.status === "ativo" ? "default" : "secondary"}>
                        {row.status}
                      </Badge>
                    </TableCell>
                    <TableCell>{row.owner}</TableCell>
                    <TableCell className="text-right">{row.conversion}%</TableCell>
                    <TableCell className="text-right">
                      <div className="flex justify-end gap-1">
                        <Dialog>
                          <Tooltip>
                            <TooltipTrigger asChild>
                              <DialogTrigger asChild>
                                <Button
                                  size="icon-sm"
                                  variant="ghost"
                                  aria-label={`Visualizar ${row.service}`}
                                >
                                  <EyeIcon />
                                </Button>
                              </DialogTrigger>
                            </TooltipTrigger>
                            <TooltipContent>Visualizar</TooltipContent>
                          </Tooltip>
                          <DialogContent>
                            <DialogHeader>
                              <DialogTitle>{row.service}</DialogTitle>
                              <DialogDescription>
                                {row.id} - {row.owner} - conversao de {row.conversion}%.
                              </DialogDescription>
                            </DialogHeader>
                          </DialogContent>
                        </Dialog>

                        <AlertDialog>
                          <Tooltip>
                            <TooltipTrigger asChild>
                              <AlertDialogTrigger asChild>
                                <Button
                                  size="icon-sm"
                                  variant="ghost"
                                  aria-label={`Deletar ${row.service}`}
                                >
                                  <Trash2Icon />
                                </Button>
                              </AlertDialogTrigger>
                            </TooltipTrigger>
                            <TooltipContent>Deletar</TooltipContent>
                          </Tooltip>
                          <AlertDialogContent>
                            <AlertDialogHeader>
                              <AlertDialogTitle>Deletar {row.service}?</AlertDialogTitle>
                              <AlertDialogDescription>
                                Esta acao remove {row.id} da tabela desta sessao de exemplo.
                              </AlertDialogDescription>
                            </AlertDialogHeader>
                            <AlertDialogFooter>
                              <AlertDialogCancel>Cancelar</AlertDialogCancel>
                              <AlertDialogAction
                                variant="destructive"
                                onClick={() =>
                                  setRemovedRowIds((currentIds) => [...currentIds, row.id])
                                }
                              >
                                Deletar
                              </AlertDialogAction>
                            </AlertDialogFooter>
                          </AlertDialogContent>
                        </AlertDialog>
                      </div>
                    </TableCell>
                  </TableRow>
                ))
              ) : (
                <TableRow>
                  <TableCell colSpan={8}>
                    <Empty className="min-h-40 border-0">
                      <EmptyHeader>
                        <EmptyMedia variant="icon">
                          <SearchIcon />
                        </EmptyMedia>
                        <EmptyTitle>Nenhum resultado</EmptyTitle>
                        <EmptyDescription>
                          Ajuste a busca ou remova filtros para voltar a ver os dados.
                        </EmptyDescription>
                      </EmptyHeader>
                    </Empty>
                  </TableCell>
                </TableRow>
              )}
            </TableBody>
          </Table>
        </div>
      </ShowcaseCard>

      <ShowcaseCard title="Graficos e tabela" description="chart, histogram/bar chart, table e progress.">
        <ChartContainer config={chartConfig} className="h-64 w-full">
          <BarChart data={chartData}>
            <CartesianGrid vertical={false} />
            <XAxis dataKey="name" tickLine={false} axisLine={false} />
            <ChartTooltip content={<ChartTooltipContent hideLabel />} />
            <Bar dataKey="volume" fill="var(--color-volume)" radius={6} />
          </BarChart>
        </ChartContainer>
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Servico</TableHead>
              <TableHead>Status</TableHead>
              <TableHead className="text-right">Aderencia</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {services.map((service) => (
              <TableRow key={service.name}>
                <TableCell className="font-medium">{service.name}</TableCell>
                <TableCell>
                  <Badge variant={service.status === "ativo" ? "default" : "secondary"}>
                    {service.status}
                  </Badge>
                </TableCell>
                <TableCell className="text-right">{service.value}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
        <Progress value={82} aria-label="Aderencia media dos servicos" />
      </ShowcaseCard>

      <ShowcaseCard title="Dados compostos" description="carousel, item, resizable e scroll-area.">
        <Carousel className="mx-auto w-full max-w-sm">
          <CarouselContent>
            {services.map((service) => (
              <CarouselItem key={service.name}>
                <Card>
                  <CardContent className="flex h-28 items-center justify-center p-6 text-sm font-medium">
                    {service.name}
                  </CardContent>
                </Card>
              </CarouselItem>
            ))}
          </CarouselContent>
          <CarouselPrevious className="left-2" />
          <CarouselNext className="right-2" />
        </Carousel>
        <ItemGroup className="rounded-lg border">
          <Item>
            <ItemMedia variant="icon">
              <CreditCardIcon />
            </ItemMedia>
            <ItemContent>
              <ItemTitle>Item de dado</ItemTitle>
              <ItemDescription>Componente Item para listas densas e repetidas.</ItemDescription>
            </ItemContent>
          </Item>
        </ItemGroup>
        <ResizablePanelGroup orientation="horizontal" className="min-h-28 rounded-lg border">
          <ResizablePanel defaultSize={55} className="flex items-center justify-center text-sm">
            Painel A
          </ResizablePanel>
          <ResizableHandle withHandle />
          <ResizablePanel defaultSize={45} className="flex items-center justify-center text-sm">
            Painel B
          </ResizablePanel>
        </ResizablePanelGroup>
        <ScrollArea className="h-28 rounded-lg border p-3">
          <div className="flex flex-col gap-2">
            {services.concat(services).map((service, index) => (
              <div key={`${service.name}-${index}`} className="rounded-md bg-muted px-3 py-2 text-sm">
                {service.name}
              </div>
            ))}
          </div>
        </ScrollArea>
      </ShowcaseCard>
    </TabsContent>
  )
}
